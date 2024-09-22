from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import CustomUser

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('rest_register')
        self.login_url = reverse('rest_login')
        self.profile_url = reverse('user-profile')
        self.user_data = {
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(email=self.user_data['email']).exists())

    def test_user_login(self):
        # First, register a user
        self.client.post(self.register_url, self.user_data)
        
        # Then, attempt to log in
        login_data = {
            'email': self.user_data['email'],
            'password': self.user_data['password1'],
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)

    def test_user_profile(self):
        # Register and log in a user
        self.client.post(self.register_url, self.user_data)
        login_response = self.client.post(self.login_url, {
            'email': self.user_data['email'],
            'password': self.user_data['password1'],
        })
        
        # Set the JWT token in the client
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {login_response.data['access_token']}")
        
        # Get user profile
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user_data['email'])

        # Update user profile
        update_data = {'first_name': 'Test', 'last_name': 'User'}
        response = self.client.put(self.profile_url, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], update_data['first_name'])
        self.assertEqual(response.data['last_name'], update_data['last_name'])
