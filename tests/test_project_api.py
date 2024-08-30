import unittest
from backend.app import app

class ProjectApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.token = "your_test_auth_token"

    def test_get_project_details(self):
        response = self.app.get('/api/project')
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        expected_keys = ['project_name', 'version', 'description']
        for key in expected_keys:
            self.assertIn(key, response_json)
        self.assertEqual(response_json['project_name'], 'ECG Signal Diagnosis')
        self.assertEqual(response_json['version'], '1.0')
        self.assertEqual(response_json['description'], 'A project to diagnose ECG signals using machine learning')

    def test_get_project_docs(self):
        response = self.app.get('/api/project/docs')
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        expected_keys = ['documentation_url']
        for key in expected_keys:
            self.assertIn(key, response_json)
        self.assertEqual(response_json['documentation_url'], 'http://example.com/docs')
