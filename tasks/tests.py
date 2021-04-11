from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()


class TaskTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='lauren', password='laurenpassword')
        url_to_login = reverse('token_obtain_pair')
        response = self.client.post(url_to_login, {'username': 'lauren', 'password': 'laurenpassword'}, follow='json')
        self.token = response.data['access']
        self.client.force_authenticate(self.user, self.token)

        self.data_task = {
            'name': 'task1',
            'description': 'task desc',
            'date_end': '2021-01-01 21:21'
        }
        self.task = self.client.post(reverse('task_create'), self.data_task)

    def test_create_task(self):
        url = reverse('task_create')
        response = self.client.post(url, self.data_task)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['name'], self.data_task['name'])
        self.assertEqual(response.data['description'], self.data_task['description'])

    def test_get_task(self):
        url = reverse('task_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data['name'], self.data_task['name'])

    def test_patch_task(self):
        url = reverse('task_detail', kwargs={'pk': 1})
        data = {'name': 'name_changed'}
        response = self.client.patch(url, data)
        self.assertEqual(data['name'], response.data['name'])

    def test_delete_task(self):
        url = reverse('task_detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
