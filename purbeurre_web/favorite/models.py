from django.db import models

from user.models import CustomUser


class Favorite(models.Model):
    """
    The products registered by the user are stored in the Favorite table.
    """
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    nutrition_grade = models.CharField(max_length=5)
    code_substitute_for = models.CharField(max_length=50)
    name_substitute_for = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    category = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
