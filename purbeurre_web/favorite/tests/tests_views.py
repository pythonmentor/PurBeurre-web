"""
Groups all the tests of the views of the FAVORITE application.
"""

from django.test import Client, TestCase
from django.urls import reverse

from favorite.models import Favorite
from user.models import CustomUser
from core.models import Category, Product


class SaveFavoriteApiViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create_user(email="test@test.com", first_name="John", password="hgfG#48")
        category = Category.objects.create(name="some_category")
        Product.objects.create(name="some_product", code="1", image_full_product_url="url",
                               nutrition_grade="d", category=category)
        Product.objects.create(name="alt_product", code="2", image_full_product_url="url",
                               nutrition_grade="a", category=category)

    def setUp(self):
        self.client = Client()

    def test_view_redirect_if_not_logged_in(self):
        response = self.client.get('/favorite/api/save_favorite/')
        self.assertRedirects(response, '/user/login/?next=/favorite/api/save_favorite/')

    def test_view_save_product_in_favorite_table(self):
        self.client.login(username="test@test.com", password="hgfG#48")
        response = self.client.post('/favorite/api/save_favorite/', {'product_code': '2',
                                                                     'product_sub_for': 'some_product'})

        product_saved = Favorite.objects.get(code='2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(product_saved.name, 'alt_product')

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('save-favorite'))
        # Status code 302 : redirection to the login page.
        self.assertEqual(response.status_code, 302)


class FavoriteListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create_user(email="test@test.com", first_name="John", password="hgfG#48")
        cls.favorite = Favorite.objects.create(name="some_product", code="1", nutrition_grade="a", user=user)

    def setUp(self):
        self.client = Client()

    def test_view_redirect_if_not_logged_in(self):
        response = self.client.get('/favorite/favorite-list/')
        self.assertRedirects(response, '/user/login/?next=/favorite/favorite-list/')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username="test@test.com", password="hgfG#48")
        response = self.client.get('/favorite/favorite-list/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username="test@test.com", password="hgfG#48")
        response = self.client.get(reverse('favorite-list'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'test@test.com')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username="test@test.com", password="hgfG#48")
        response = self.client.get(reverse('favorite-list'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'test@test.com')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorite-list.html')

    def test_view_alt_product_in_the_context(self):
        self.client.login(username="test@test.com", password="hgfG#48")
        response = self.client.get(reverse('favorite-list'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'test@test.com')
        self.assertEqual(response.context['favorite_list'].count(), 1)
