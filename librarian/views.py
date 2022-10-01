from functools import partial
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Account
from book.models import Book
from book.serializers import BookSerilaizer
from librarian.serializer import LibrarianLoginSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from accounts.serializers import AccountSerializer


class LoginLibrarian(APIView):
    def post(self, request):
        serializer = LibrarianLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = authenticate(username=data["username"], password=data["password"])
        if not user.is_admin:
            raise serializers.ValidationError("You are not an Authorized")

        refresh = RefreshToken.for_user(user)
        return Response({"access": str(refresh.access_token), "refresh": str(refresh)})


class AddBook(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        book = BookSerilaizer(data=request.data)
        if book.is_valid():
            book.save()
            return Response(book.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class EditBook(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def patch(self, request, id):
        book = Book.objects.get(id=id)
        serializer = BookSerilaizer(instance=book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(400)


class DeleteBook(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, id):
        book = Book.objects.get(id=id)
        book.delete()
        return Response(status=status.HTTP_200_OK)


class AllMember(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        members = Account.objects.all()
        serializer = AccountSerializer(members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddMember(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class EditMember(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def patch(self, request, id):
        member = Account.objects.get(id=id)
        serializer = AccountSerializer(instance=member, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteMember(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, id):
        member = Account.objects.get(id=id)
        member.delete()
        return Response(status=status.HTTP_200_OK)
