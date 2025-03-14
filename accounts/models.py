from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
from books.models import Book


# Create your models here.

# class Create_user(models.Model):
#     username = models.CharField(max_length=16, blank=False, null=False, unique=True)
#     email = models.EmailField(_('email address'), unique=True)
#     phone_no = models.CharField(default='1234567890', max_length=11, blank=True, null=True, unique=True)
#     user_permissions = models.ManyToManyField('auth.Permission', related_name='customer_permissions', blank=True, )
#     groups = models.ManyToManyField('auth.Group', related_name='customer_groups', blank=True, )
#

class Login(AbstractUser):
    username = models.CharField(max_length=16, blank=False, null=False, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    phone_no = models.CharField(default='1234567890', max_length=11, blank=True, null=True, unique=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customer_permissions', blank=True, )
    groups = models.ManyToManyField('auth.Group', related_name='customer_groups', blank=True, )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'email']

    @staticmethod
    def check_user_details(email, username, phone_no):
        try:
            if Login.objects.filter(email=email).exists():
                return f"Email {email} is already registered."

            if Login.objects.filter(username=username).exists():
                return f"Username {username} is already registered."

            if Login.objects.filter(phone_no=phone_no).exists():
                return f"Phone number {phone_no} is already registered."

            return "None of the provided details exist in the database. You can proceed."

        except Exception as e:
            return f"An error occurred: {str(e)}"

    def __str__(self):
        return "{}".format(self.email, self.username, self.phone_no)


class Library(models.Model):
    title = models.CharField(max_length=16)
    shelf = models.ForeignKey(
        Book,
        related_name='library',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title}, {self.shelf}"


# class Wallet(models.Model):
#     pass


# class UserInformation(models.Model):
#     pass


class Address(models.Model):
    CITY_NAME = [
        (1, 'TEHRAN'),
        (2, 'SHIRAZ'),
        (3, 'KARAJ'),
        (4, 'GAZVIN'),
    ]
    city = models.PositiveIntegerField(
        choices=CITY_NAME,
        null=False, blank=False,

    )
    addr = models.CharField(
        max_length=128,
        blank=False, null=False,
                            )


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} - {self.created_at}"


class RequestProduct(models.Model):
    book_title = models.CharField(max_length=32)
    auther_name = models.CharField(max_length=32)
