from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Account
from accounts.serializers import AccountSerializer
from django.contrib.auth import logout
from book.models import Book, BookBorrow, BookReturn
from book.serializers import BookBorrowSerilaizer, ReturnBookSerializer
from member.serializers import MemberLoginrSerializer
from rest_framework.permissions import IsAuthenticated


class RegisterMember(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LoginMemeber(APIView):
    def post(self, request):
        serializer = MemberLoginrSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = authenticate(username=data["username"], password=data["password"])
        if user is None:
            raise serializers.ValidationError("Wrong Crednetials")
        refresh = RefreshToken.for_user(user)
        return Response({"access": str(refresh.access_token), "refresh": str(refresh)})


class DeleteAccount(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        user = Account.objects.get(id=id)
        user.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)


class BorrowBook(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        member = Account.objects.get(id=data["member"])
        book_name = Book.objects.get(id=data["book"])
        if BookBorrow.objects.filter(member__id=data["member"]).exists():
            book_borrow = BookBorrow.objects.get(member__id=data["member"])
            book_borrow.book.add(book_name)
            book_name.borrowed = True
            book_name.save()
        else:
            book_borrow = BookBorrow.objects.create(member=member)
            book_borrow.book.add(book_name)
            book_name.borrowed = True
            book_name.save()
        serializer = BookBorrowSerilaizer(book_borrow)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReturnBook(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        book_name = Book.objects.get(id=data["book"])
        member = BookBorrow.objects.get(id=data["borrow"])
        member_name = BookReturn.objects.create(borrow=member)
        book_return = member_name.borrow.book.get(id=data["book"])
        book_return.save()
        book_name.available = True
        book_name.borrowed = False
        book_name.save()
        serializer = ReturnBookSerializer(member_name)

        return Response(serializer.data, status=status.HTTP_200_OK)
