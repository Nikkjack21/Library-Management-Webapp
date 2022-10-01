from django.urls import path

from .views import BorrowBook, DeleteAccount, LoginMemeber, RegisterMember, ReturnBook

urlpatterns = [
    # member-auth
    path("register", RegisterMember.as_view()),
    path("login", LoginMemeber.as_view()),
    path("delete/<int:id>", DeleteAccount.as_view()),
    # member-book
    path("borrow", BorrowBook.as_view()),
    path("return", ReturnBook.as_view()),
]
