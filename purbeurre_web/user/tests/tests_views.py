"""
Groups all the tests of the views of the USER application.
"""

from django.test import Client, TestCase
from django.urls import reverse

from user.models import CustomUser


class LoginViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create_user(email="test@test.com", first_name="John", password="hgfG#48")

    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/user/login/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_view_user_logged_in(self):
        login = self.client.login(username="test@test.com", password="hgfG#48")
        self.assertTrue(login)

    def test_view_after_login_user_redirected_to_index_page(self):
        response = self.client.post('/user/login/', {'username': 'test@test.com', 'password': 'hgfG#48'})
        # After login the user is redirected to the index page.
        self.assertRedirects(response, '/')

    def test_view_when_the_password_is_not_correct(self):
        response = self.client.post('/user/login/', {'username': 'test@test.com', 'password': 'xxxx'})
        # When the password is not correct, user remains on the login page.
        page = response.template_name[0]
        self.assertEqual(page, 'registration/login.html')


class SignUpViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/user/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_view_after_creation_user_redirected_to_index_page(self):
        response = self.client.post('/user/signup/', {'email': 'test@test.com',
                                                      'first_name': 'John',
                                                      'password1': 'hgfG#48',
                                                      'password2': 'hgfG#48'})
        # After login the user is redirected to the index page.
        self.assertRedirects(response, '/')

    def test_view_when_password_1_2_not_match(self):
        response = self.client.post('/user/signup/', {'email': 'test@test.com',
                                                      'first_name': 'John',
                                                      'password1': 'hgfG#48',
                                                      'password2': 'xxxx'})
        # When password 1 & 2 do not match, user remains on the signup page.
        page = response.template_name[0]
        self.assertEqual(page, 'signup.html')


class AccountViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create_user(email="test@test.com", first_name="John", password="hgfG#48")

    def setUp(self):
        self.client = Client()

    def test_view_redirect_if_not_logged_in(self):
        response = self.client.get('/user/account/')
        self.assertRedirects(response, '/user/login/?next=/user/account/')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username="test@test.com", password="hgfG#48")
        response = self.client.get('/user/account/')
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'test@test.com')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username="test@test.com", password="hgfG#48")
        response = self.client.get(reverse('account'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'test@test.com')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username="test@test.com", password="hgfG#48")
        response = self.client.get(reverse('account'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'test@test.com')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')

    def test_view_first_name_in_the_context(self):
        self.client.login(username="test@test.com", password="hgfG#48")
        response = self.client.get(reverse('account'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'test@test.com')
        self.assertEqual(response.context['user'].first_name, 'John')
