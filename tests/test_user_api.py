import unittest
from backend.app import app
import json

class UserApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.token = "your_test_auth_token"

    def test_register_user(self):
        request_body = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com"
        }
        response = self.app.post('/api/users/register', 
                                 data=json.dumps(request_body), 
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        self.assertIn('success', response_json)
        self.assertIn('message', response_json)
        self.assertTrue(response_json['success'])
        self.assertEqual(response_json['message'], 'User registered successfully.')

    def test_user_login(self):
        login_data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.app.post('/api/users/login', json=login_data)
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        self.assertIn('success', response_json)
        self.assertIn('token', response_json)
        self.assertTrue(response_json['success'])
        self.assertIsInstance(response_json['token'], str)

    def test_get_user_profile(self):
        response = self.app.get(
            '/api/users/profile',
            headers={'Authorization': f'Bearer {self.token}'}
        )
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        expected_keys = ['username', 'email', 'profile_data']
        for key in expected_keys:
            self.assertIn(key, response_json)
        self.assertEqual(response_json['username'], 'sample_user')
        self.assertEqual(response_json['email'], 'user@example.com')
        self.assertEqual(response_json['profile_data'], {})
