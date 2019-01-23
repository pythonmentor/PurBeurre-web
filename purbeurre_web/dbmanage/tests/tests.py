from django.test import TestCase
from django.core.management import call_command
from io import StringIO
from unittest.mock import patch, Mock

from dbmanage.tests.mockapi import mock_api_return
from core.models import Category, Product


class DatabaseCommandTest(TestCase):
    """
    Test for the database management command.
    """

    @patch('requests.get')
    def test_command_populate(self, mock_get_products):
        """
        Test for the command : python manage.py database --populate
        """

        mock_get_products.return_value = Mock()
        mock_get_products.return_value.json.return_value = mock_api_return

        out = StringIO()
        call_command('database', '--populate', stdout=out)

        category_count = Category.objects.all().count()
        product_count = Product.objects.all().count()

        self.assertTrue(category_count >= 1)
        self.assertTrue(product_count >= 1)
        self.assertIn('Database populated', out.getvalue())

    @patch('requests.get')
    def test_command_delete(self, mock_get_products):
        """
        Test for the command : python manage.py database --delete
        """

        mock_get_products.return_value = Mock()
        mock_get_products.return_value.json.return_value = mock_api_return

        # Register a category for the test.
        cat = Category(name='test_category')
        cat.save()

        # Register a product for the test.
        Product(name='prod_name',
                code='1',
                nutrition_grade='a',
                image_nutrition_url='image_nutrition_url',
                image_small_product_url='image_small_product_url',
                image_full_product_url='image_full_product_url',
                url='url',
                category=cat).save()

        category_count_before_del = Category.objects.all().count()
        product_count_before_del = Product.objects.all().count()

        out = StringIO()
        call_command('database', '--delete', stdout=out)

        category_count_after_del = Category.objects.all().count()
        product_count_after_del = Product.objects.all().count()

        # Before delete
        self.assertEqual(category_count_before_del, 1)
        self.assertEqual(product_count_before_del, 1)

        # After delete
        self.assertEqual(category_count_after_del, 0)
        self.assertEqual(product_count_after_del, 0)

        self.assertIn('1 products and 1 categories deleted', out.getvalue())
