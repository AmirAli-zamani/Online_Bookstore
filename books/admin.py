from django.contrib import admin
from .models import Product, Book, Category, Author, Review
from django.contrib.admin import register


# Register your models here.

@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_time', 'description', 'category']
    search_fields = ['title', 'author__name']
    list_filter = ['category']
    is_active = True

@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']
    list_per_page = 10

@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'description']

@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'ups', 'description']#, 'review']
    list_filter = ['category']
    list_per_page = 10
    is_active = True


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'rate', 'comment')
    list_filter = ['rate']