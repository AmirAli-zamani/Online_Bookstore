from django.contrib.admin import register
from django.contrib import admin
from .models import Login, Library, Address, Comment, RequestProduct

# Register your models here.

@register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ['username', 'email','phone_no', 'USERNAME_FIELD']
    # list_per_page = [20]
    is_active = True

@register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['title', 'shelf']
    list_filter = ['shelf']
    is_active = True

@register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['city', 'addr']
    list_filter = ['city']

@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'created_at']
    list_filter = ['user']
    is_active = True

@register(RequestProduct)
class RequestProductAdmin(admin.ModelAdmin):
    list_display = ['book_title', 'auther_name']
    # list_per_page = [20]
    is_active = True