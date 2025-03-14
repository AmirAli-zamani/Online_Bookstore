from django.db import models


# ------------------------------------------
# Product Type Model
# ------------------------------------------
# class ProductType(models.Model):
#     title = models.CharField(max_length=32, blank=False, null=False)
#     created_time = models.DateTimeField(auto_now_add=True)
#     # modified_time = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = "Product Type"
#         verbose_name_plural = "Product Types"
#
#     def __str__(self):
#         return f'{self.title}, {self.created_time} '

# ------------------------------------------
# Category Model
# ------------------------------------------
class Category(models.Model):
    name = models.CharField(max_length=32, unique=True, default='Unknown')
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.name}, {self.description[:30]} '


# ------------------------------------------
# Author Model
# ------------------------------------------
class Author(models.Model):
    name = models.CharField(max_length=32, unique=True, default='Unknown')
    description = models.CharField(max_length=256, blank=True, null=True)
    age = models.PositiveIntegerField(blank=False, null=False)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return f'{self.name}, {self.description[:30]}, {self.age}  '


# ------------------------------------------
# Book Model
# ------------------------------------------
class Book(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)  # افزودن max_length
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='books'
    )
    price = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)

    # modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f'{self.title} (${self.price}) {self.description[:100]}'


# ------------------------------------------
# Review
# ------------------------------------------
class Review(models.Model):
    RATE_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]

    title = models.CharField(max_length=100)
    comment = models.TextField()
    rate = models.IntegerField(
        choices=RATE_CHOICES,
        default=0
    )

    def __str__(self):
        return f"{self.title} - {self.rate} Star,{self.comment}"


# ------------------------------------------
# Product Model
# ------------------------------------------
class Product(models.Model):
    title = models.CharField(max_length=32)
    ups = models.BigIntegerField(unique=True)
    description = models.TextField(blank=True, null=True)

    # product_type = models.ForeignKey(
    #     ProductType,
    #     on_delete=models.PROTECT,
    #     related_name="products"
    # )

    # review = models.ForeignKey(
    #     Review,
    #     on_delete=models.PROTECT,
    #     related_name="products"
    # )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products'
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name='products'
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name='products'
    )

    def __str__(self):
        return f"{self.title} - {self.ups} - "
