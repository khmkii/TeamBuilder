import datetime
from django.core.urlresolvers import reverse_lazy
from django.test import TestCase, Client
from . import models, forms


class AccountsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = models.SiteUser.users.create_user(
            email='test_user1@email.com',
            username='testuser1',
            password='testpassword'
        )
        cls.super_user = models.SiteUser.users.create_superuser(
            email='test_superuser1@email.com',
            username='testsuperuser1',
            password='testsuperpassword',
        )

    def test_user_creation(self):
        self.assertEqual(
            [self.user.username, self.user.email],
            ['testuser1', 'test_user1@email.com']
        )
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertIsInstance(self.user.profile, models.Profile)
        self.assertIsInstance(self.user.date_joined, datetime.datetime)
        self.assertEqual(self.user.get_full_name(), f'{self.user.username} {self.user.email}')
        self.assertEqual(self.user.get_short_name(), f'{self.user.username}')

    def test_superuser_creation(self):
        self.assertEqual(
            [self.super_user.username, self.super_user.email],
            ['testsuperuser1', 'test_superuser1@email.com']
        )
        self.assertTrue(self.super_user.is_staff)
        self.assertTrue(self.super_user.is_active)
        self.assertIsInstance(self.super_user.profile, models.Profile)

    def test_profile_creation(self):
        pass


class AccountsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.login_url = reverse_lazy('accounts:login')
        cls.sign_up_url = reverse_lazy('accounts:sign_up')
        cls.logout_url = reverse_lazy('accounts:logout')

    def test_login_view_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='accounts/login.html')

    def test_signup_view_get(self):
        response = self.client.get(self.sign_up_url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], forms.UserCreationForm)
