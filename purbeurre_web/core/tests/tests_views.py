"""
Groups all the tests of the views of the CORE application.
"""

from django.test import Client, TestCase
from django.urls import reverse
from urllib.parse import urlencode

from core.models import Product, Category


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class ContactViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')


class LegalNoticeViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/legal-notice/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('legal-notice'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('legal-notice'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'legal-notice.html')


class AlternativeProductsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name="some_category")
        cls.product_d = Product.objects.create(name="some_product_d", code="1", image_full_product_url="url_d",
                                               nutrition_grade="d", category=category)
        cls.product_a = Product.objects.create(name="some_product_a", code="2", image_full_product_url="url_a",
                                               nutrition_grade="a", category=category)

    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/alt-prod/?product='+self.product_d.name)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        base_url = reverse('alt-prod')
        query_string = urlencode({'product': self.product_d.name})
        url = f'{base_url}?{query_string}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/alt-prod/?product=' + self.product_d.name)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products-alt.html')

    def test_view_returns_404_when_search_not_specified(self):
        response = self.client.get('/alt-prod/?product=')
        self.assertEqual(response.status_code, 404)

    def test_view_returns_404_when_get_method_not_used(self):
        response = self.client.get('/prod-details/')
        self.assertEqual(response.status_code, 404)

    def test_view_alt_product_in_the_context(self):
        response = self.client.get('/alt-prod/?product=' + self.product_d.name)
        self.assertEquals(response.context['products_alt'].count(), 1)

    def test_view_search_product_in_the_context(self):
        response = self.client.get('/alt-prod/?product=' + self.product_d.name)
        self.assertEquals(response.context['search_product'], 'Some_product_d')

    def test_view_search_product_img_in_the_context(self):
        response = self.client.get('/alt-prod/?product=' + self.product_d.name)
        self.assertEquals(response.context['search_product_img_url'], 'url_d')


class ProductDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name="some_category")
        cls.product = Product.objects.create(name="some_product", code="1", category=category)

    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/prod-details/' + self.product.code + '/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('prod-details', args=(self.product.code,)))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('prod-details', args=(self.product.code,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_details.html')

    def test_view_returns_404_when_product_not_exist(self):
        response = self.client.get(reverse('prod-details', args=('x',)))
        self.assertEqual(response.status_code, 404)

    def test_view_returns_404_when_product_not_specify(self):
        response = self.client.get('/prod-details/')
        self.assertEqual(response.status_code, 404)


class GetProductsApiViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/api/get_products/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('get_products'))
        self.assertEqual(response.status_code, 200)
