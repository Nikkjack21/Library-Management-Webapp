# Generated by Django 4.1.1 on 2022-09-30 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookBorrow",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("borrow", models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="borrowed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="book",
            name="returned",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="BookReturn",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("returned", models.BooleanField(default=False)),
                (
                    "borrow",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="book.bookborrow",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="bookborrow",
            name="book",
            field=models.ManyToManyField(to="book.book"),
        ),
        migrations.AddField(
            model_name="bookborrow",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]