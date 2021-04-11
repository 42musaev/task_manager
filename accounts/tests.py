from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()


class AccountsTest(APITestCase):

    def setUp(self):
        url = reverse('account_register')
        data = {
            'username': 'test_user',
            'password': 'test_password',
            'full_name': 'test_full_name'
        }
        self.response = self.client.post(url, data, follow='json')
        self.user = User.objects.get(username='test_user')

    def test_register_account(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test_user')

    def test_login_user(self):
        data = {
            'username': 'test_user',
            'password': 'test_password',
        }
        url = reverse('token_obtain_pair')
        response = self.client.post(url, data, follow='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
