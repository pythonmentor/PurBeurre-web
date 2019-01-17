from django.db import models


class Category(models.Model):
    """
    Categories are saved in the Category table.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    The products are saved in the Product table.
    Each product is associated with a category.
    """
    name = models.CharField(max_length=200)
    code = models.CharField(primary_key=True, max_length=50)
    nutrition_grade = models.CharField(max_length=5)
    image_nutrition_url = models.CharField(max_length=500)
    image_small_product_url = models.CharField(max_length=500)
    image_full_product_url = models.CharField(max_length=500)
    url = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
