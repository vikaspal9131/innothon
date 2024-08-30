import unittest
from backend.app import app

class ModelApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_model_metrics(self):
        response = self.app.get('/api/model/metrics')
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        expected_keys = ['accuracy', 'precision', 'recall', 'f1_score']
        for key in expected_keys:
            self.assertIn(key, response_json)
        self.assertTrue(isinstance(response_json['accuracy'], (int, float)))
        self.assertTrue(isinstance(response_json['precision'], (int, float)))
        self.assertTrue(isinstance(response_json['recall'], (int, float)))
        self.assertTrue(isinstance(response_json['f1_score'], (int, float)))

    def test_get_model_details(self):
        response = self.app.get('/api/model')
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        expected_keys = ['model_version', 'description', 'last_update']
        for key in expected_keys:
            self.assertIn(key, response_json)
        self.assertEqual(response_json['model_version'], '1.0')
        self.assertEqual(response_json['description'], 'Description of the model')
        self.assertIn('last_update', response_json)
