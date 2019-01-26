"""
Groups all the tests of the models of the CORE application.
"""

from django.test import TestCase

from core.models import Product, Category


class CategoryModelTest(TestCase):
    """
    Test the Category model.
    """
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="some_category")

    # Test name field
    def test_model_name_field_type(self):
        field_type = self.category._meta.get_field('name').get_internal_type()
        self.assertEquals(field_type, 'CharField')

    def test_model_name_field_max_length(self):
        max_length = self.category._meta.get_field('name').max_length
        self.assertTrue(max_length >= 50)

    def test_model_name_field_label(self):
        field_label = self.category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    # Test __str__ method
    def test_model_str(self):
        self.assertEquals(str(self.category), 'some_category')


class ProductModelTest(TestCase):
    """
    Test the Product model.
    """
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name="some_category")
        cls.product = Product.objects.create(name="some_product", code="1", image_full_product_url="url",
                                             nutrition_grade="a", category=category)

    # Test name field
    def test_model_name_field_type(self):
        field_type = self.product._meta.get_field('name').get_internal_type()
        self.assertEquals(field_type, 'CharField')

    def test_model_name_field_max_length(self):
        max_length = self.product._meta.get_field('name').max_length
        self.assertTrue(max_length >= 200)

    def test_model_name_field_label(self):
        field_label = self.product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    # Test code field
    def test_model_code_field_type(self):
        field_type = self.product._meta.get_field('code').get_internal_type()
        self.assertEquals(field_type, 'CharField')

    def test_model_code_field_is_pk(self):
        self.assertEquals(self.product.pk, '1')

    def test_model_code_field_max_length(self):
        max_length = self.product._meta.get_field('code').max_length
        self.assertTrue(max_length >= 50)

    def test_model_code_field_label(self):
        field_label = self.product._meta.get_field('code').verbose_name
        self.assertEquals(field_label, 'code')

    # Test nutrition_grade field
    def test_model_nutrition_grade_field_type(self):
        field_type = self.product._meta.get_field('nutrition_grade').get_internal_type()
        self.assertEquals(field_type, 'CharField')

    def test_model_nutrition_grade_field_max_length(self):
        max_length = self.product._meta.get_field('nutrition_grade').max_length
        self.assertTrue(max_length >= 5)

    def test_model_nutrition_grade_field_label(self):
        field_label = self.product._meta.get_field('nutrition_grade').verbose_name
        self.assertEquals(field_label, 'nutrition grade')

    # Test image_nutrition_url field
    def test_model_image_nutrition_url_field_type(self):
        field_type = self.product._meta.get_field('image_nutrition_url').get_internal_type()
        self.assertEquals(field_type, 'CharField')

    def test_model_image_nutrition_url_field_max_length(self):
        max_length = self.product._meta.get_field('image_nutrition_url').max_length
        self.assertTrue(max_length >= 500)

    def test_model_image_nutrition_url_field_label(self):
        field_label = self.product._meta.get_field('image_nutrition_url').verbose_name
        self.assertEquals(field_label, 'image nutrition url')

    # Test image_small_product_url field
    def test_model_image_small_product_url_field_type(self):
        field_type = self.product._meta.get_field('image_small_product_url').get_internal_type()
        self.assertEquals(field_type, 'CharField')

    def test_model_image_small_product_url_field_max_length(self):
        max_length = self.product._meta.get_field('image_small_product_url').max_length
        self.assertTrue(max_length >= 500)

    def test_model_image_small_product_url_field_label(self):
        field_label = self.product._meta.get_field('image_small_product_url').verbose_name
        self.assertEquals(field_label, 'image small product url')

    # Test image_full_product_url field
    def test_model_image_full_product_url_field_type(self):
        field_type = self.product._meta.get_field('image_full_product_url').get_internal_type()
        self.assertEquals(field_type, 'CharField')

    def test_model_image_full_product_url_field_max_length(self):
        max_length = self.product._meta.get_field('image_full_product_url').max_length
        self.assertTrue(max_length >= 500)

    def test_model_image_full_product_url_field_label(self):
        field_label = self.product._meta.get_field('image_full_product_url').verbose_name
        self.assertEquals(field_label, 'image full product url')

    # Test url field
    def test_model_url_field_type(self):
        field_type = self.product._meta.get_field('url').get_internal_type()
        self.assertEquals(field_type, 'CharField')

    def test_model_url_field_max_length(self):
        max_length = self.product._meta.get_field('url').max_length
        self.assertTrue(max_length >= 300)

    def test_model_url_field_label(self):
        field_label = self.product._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'url')

    # Test category field
    def test_model_category_field_type(self):
        field_type = self.product._meta.get_field('category').get_internal_type()
        self.assertEquals(field_type, 'ForeignKey')

    def test_model_category_field_is_category_obj(self):
        self.assertTrue(isinstance(self.product.category, Category))

    def test_model_category_field_label(self):
        field_label = self.product._meta.get_field('category').verbose_name
        self.assertEquals(field_label, 'category')

    # Test __str__ method
    def test_model_str(self):
        self.assertEquals(str(self.product), 'some_product')
