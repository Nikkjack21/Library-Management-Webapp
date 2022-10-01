from email.policy import default
from django.db import models

from accounts.models import Account

# Create your models here.


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    borrowed = models.BooleanField(default=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.book_name


class BookBorrow(models.Model):
    member = models.ForeignKey(Account, on_delete=models.PROTECT)
    book = models.ManyToManyField(Book)

    class Meta:
        verbose_name = "Book borrows"
        verbose_name_plural = "Book borrow"

    def __str__(self):
        return self.member.username


class BookReturn(models.Model):
    borrow = models.ForeignKey(BookBorrow, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Book returns"
        verbose_name_plural = "Book return"

    def __str__(self):
        return str(self.borrow.member)
