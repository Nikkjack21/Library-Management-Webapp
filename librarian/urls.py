from django.urls import path
from .views import (
    AddBook,
    AddMember,
    AllMember,
    DeleteBook,
    DeleteMember,
    EditBook,
    EditMember,
    LoginLibrarian,
)

urlpatterns = [
    path("login", LoginLibrarian.as_view()),
    # book-crud
    path("add-book", AddBook.as_view()),
    path("edit-book/<int:id>", EditBook.as_view()),
    path("delete-book/<int:id>", DeleteBook.as_view()),
    # member-crud
    path("all-member", AllMember.as_view()),
    path("add-member", AddMember.as_view()),
    path("edit-member/<int:id>", EditMember.as_view()),
    path("delete-member/<int:id>", DeleteMember.as_view()),
]
