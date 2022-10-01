
from rest_framework.serializers import ModelSerializer

from accounts.serializers import AccountSerializer
from .models import Book, BookBorrow, BookReturn


class BookSerilaizer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookBorrowSerilaizer(ModelSerializer):
    member = AccountSerializer
    book = BookSerilaizer(read_only=True, many=True)

    class Meta:
        model = BookBorrow
        fields = "__all__"

class ReturnBookSerializer(ModelSerializer):
    member = BookBorrowSerilaizer
    class Meta:
        model = BookReturn
        fields='__all__'

    
