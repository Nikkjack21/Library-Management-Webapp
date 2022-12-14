# Generated by Django 4.1.1 on 2022-09-30 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0002_bookborrow_book_borrowed_book_returned_bookreturn_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookborrow",
            options={
                "verbose_name": "Book borrows",
                "verbose_name_plural": "Book borrow",
            },
        ),
        migrations.AlterModelOptions(
            name="bookreturn",
            options={
                "verbose_name": "Book returns",
                "verbose_name_plural": "Book return",
            },
        ),
        migrations.RemoveField(
            model_name="bookborrow",
            name="borrow",
        ),
        migrations.RemoveField(
            model_name="bookreturn",
            name="returned",
        ),
    ]
