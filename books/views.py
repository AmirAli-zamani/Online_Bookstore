from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Review


# Create your views here.
def product_list(request):
    context = dict()
    context['products'] = Product.objects.select_related('category').all()
    return render(request, 'books/product_list.html', context)


