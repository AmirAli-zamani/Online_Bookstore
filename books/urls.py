from django.urls import path
from .views import product_list #, category_list, author_list

urlpatterns = [
    path('product/list/', product_list, name='product-list'),
    ]
#     path('category/list', category_list, name='category-list'),
#     path('author/list', author_list, name='author-list'),
# ]
