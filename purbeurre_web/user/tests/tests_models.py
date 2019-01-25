"""
Groups all the tests of the models of the USER application.
"""

from django.test import TestCase

from user.models import CustomUser, CustomUserManager


class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(email="test@test.com", first_name="John", password="hgfG#48")

    # Test email field
    def test_model_email_field_type(self):
        field_type = CustomUser._meta.get_field('email').get_internal_type()
        self.assertEqual(field_type, 'CharField')

    def test_model_email_field_max_length(self):
        max_length = CustomUser._meta.get_field('email').max_length
        self.assertTrue(max_length >= 255)

    def test_model_email_field_label(self):
        field_label = CustomUser._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_model_email_field_is_unique(self):
        field_unique = CustomUser._meta.get_field('email').unique
        self.assertTrue(field_unique)

    # Test first_name field
    def test_model_first_name_field_type(self):
        field_type = CustomUser._meta.get_field('first_name').get_internal_type()
        self.assertEqual(field_type, 'CharField')

    def test_model_first_name_field_max_length(self):
        max_length = CustomUser._meta.get_field('first_name').max_length
        self.assertTrue(max_length >= 30)

    def test_model_first_name_field_label(self):
        field_label = CustomUser._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'Prénom')

    # Test is_active field
    def test_model_is_active_field_type(self):
        field_type = CustomUser._meta.get_field('is_active').get_internal_type()
        self.assertEqual(field_type, 'BooleanField')

    def test_model_is_active_field_default_value(self):
        default_value = CustomUser._meta.get_field('is_active').default
        self.assertTrue(default_value)

    def test_model_is_active_field_label(self):
        field_label = CustomUser._meta.get_field('is_active').verbose_name
        self.assertEqual(field_label, 'is active')

    # Test is_admin field
    def test_model_is_admin_field_type(self):
        field_type = CustomUser._meta.get_field('is_admin').get_internal_type()
        self.assertEqual(field_type, 'BooleanField')

    def test_model_is_admin_field_default_value(self):
        default_value = CustomUser._meta.get_field('is_admin').default
        self.assertFalse(default_value)

    def test_model_is_admin_field_label(self):
        field_label = CustomUser._meta.get_field('is_admin').verbose_name
        self.assertEqual(field_label, 'is admin')

    # Test CustomUser.objects is  a CustomUserManager() object
    def test_model_custom_user_manager_obj(self):
        self.assertTrue(isinstance(CustomUser.objects, CustomUserManager))

    # Test __str__ method
    def test_model_str(self):
        self.assertEqual(str(self.user), 'test@test.com')


class CustomUserManagerModelTest(TestCase):

    # Test create user.
    def test_model_create_user(self):
        CustomUser.objects.create_user(email="test@test.com", first_name="John", password="hgfG#48")
        user = CustomUser.objects.get(email='test@test.com')
        self.assertEqual(user.first_name, 'John')
        self.assertFalse(user.is_staff)

    # Test create super user.
    def test_model_create_super_user(self):
        CustomUser.objects.create_superuser(email="super-test@test.com", first_name="Super John", password="hgfG#48")
        super_user = CustomUser.objects.get(email='super-test@test.com')
        self.assertEqual(super_user.first_name, 'Super John')
        self.assertTrue(super_user.is_staff)
