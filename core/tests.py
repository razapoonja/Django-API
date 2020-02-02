from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

User = get_user_model()

class PostTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='TestUser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_get_posts_authenticated(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_posts_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
