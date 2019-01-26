"""
Groups all the tests of the models of the FAVORITE application.
"""

from django.test import TestCase

from favorite.models import Favorite
from user.models import CustomUser


class FavoriteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create(email="test@test.com", first_name="John")
        cls.favorite = Favorite.objects.create(name="some_product", code="1", nutrition_grade="a", user=user)

    # Test name field
    def test_model_name_field_type(self):
        field_type = self.favorite._meta.get_field('name').get_internal_type()
        self.assertEquals(field_type, 'CharField')

    def test_model_name_field_max_length(self):
        max_length = self.favorite._meta.get_field('name').max_length
        self.assertTrue(max_length >= 200)

    def test_model_name_field_label(self):
        field_label = self.favorite._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    # Test code field
    def test_model_code_field_type(self):
        field_type = self.favorite._meta.get_field('code').get_internal_type()
        self.assertEquals(field_type, 'CharField')

    def test_model_code_field_max_length(self):
        max_length = self.favorite._meta.get_field('code').max_length
        self.assertTrue(max_length >= 50)

    def test_model_code_field_label(self):
        field_label = self.favorite._meta.get_field('code').verbose_name
        self.assertEquals(field_label, 'code')

    # Test nutrition_grade field
    def test_model_nutrition_grade_field_type(self):
        field_type = self.favorite._meta.get_field('nutrition_grade').get_internal_type()
        self.assertEquals(field_type, 'CharField')

    def test_model_nutrition_grade_field_max_length(self):
        max_length = self.favorite._meta.get_field('nutrition_grade').max_length
        self.assertTrue(max_length >= 5)

    def test_model_nutrition_grade_field_label(self):
        field_label = self.favorite._meta.get_field('nutrition_grade').verbose_name
        self.assertEquals(field_label, 'nutrition grade')

    # Test code_substitute_for field
    def test_model_code_substitute_for_field_type(self):
        field_type = self.favorite._meta.get_field('code_substitute_for').get_internal_type()
        self.assertEquals(field_type, 'CharField')

    def test_model_code_substitute_for_field_max_length(self):
        max_length = self.favorite._meta.get_field('code_substitute_for').max_length
        self.assertTrue(max_length >= 50)

    def test_model_code_substitute_for_field_label(self):
        field_label = self.favorite._meta.get_field('code_substitute_for').verbose_name
        self.assertEquals(field_label, 'code substitute for')

    # Test name_substitute_for field
    def test_model_name_substitute_for_field_type(self):
        field_type = self.favorite._meta.get_field('name_substitute_for').get_internal_type()
        self.assertEquals(field_type, 'CharField')

    def test_model_name_substitute_for_field_max_length(self):
        max_length = self.favorite._meta.get_field('name_substitute_for').max_length
        self.assertTrue(max_length >= 200)

    def test_model_name_substitute_for_field_label(self):
        field_label = self.favorite._meta.get_field('name_substitute_for').verbose_name
        self.assertEquals(field_label, 'name substitute for')

    # Test url field
    def test_model_url_field_type(self):
        field_type = self.favorite._meta.get_field('url').get_internal_type()
        self.assertEquals(field_type, 'CharField')

    def test_model_url_field_max_length(self):
        max_length = self.favorite._meta.get_field('url').max_length
        self.assertTrue(max_length >= 300)

    def test_model_url_field_label(self):
        field_label = self.favorite._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'url')

    # Test category field
    def test_model_category_field_type(self):
        field_type = self.favorite._meta.get_field('category').get_internal_type()
        self.assertEquals(field_type, 'CharField')

    def test_model_category_field_max_length(self):
        max_length = self.favorite._meta.get_field('category').max_length
        self.assertTrue(max_length >= 50)

    def test_model_category_field_label(self):
        field_label = self.favorite._meta.get_field('category').verbose_name
        self.assertEquals(field_label, 'category')

    # Test user field
    def test_model_user_field_type(self):
        field_type = self.favorite._meta.get_field('user').get_internal_type()
        self.assertEquals(field_type, 'ForeignKey')

    def test_model_user_field_is_customuser_obj(self):
        self.assertTrue(isinstance(self.favorite.user, CustomUser))

    def test_model_user_field_label(self):
        field_label = self.favorite._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'user')

    # Test __str__ method
    def test_model_str(self):
        self.assertEquals(str(self.favorite), 'some_product')
