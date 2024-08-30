import unittest
import io
import json
from backend.app import app

class ECGApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.token = "your_test_auth_token"

    def test_get_ecg_images(self):
        response = self.app.get('/api/ecg/images')
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        self.assertIsInstance(response_json, list)
        expected_images = [
            {"image_name": "image1.png", "image_url": "http://example.com/image1.png"},
            {"image_name": "image2.png", "image_url": "http://example.com/image2.png"}
        ]
        self.assertEqual(response_json, expected_images)

    def test_get_ecg_diagnosis(self):
        file_id = "example_file_id"
        response = self.app.get(f'/api/ecg/diagnosis/{file_id}', headers={
            'Authorization': f'Bearer {self.token}'
        })
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        expected_keys = ['diagnosis', 'status']
        for key in expected_keys:
            self.assertIn(key, response_json)
        diagnosis = response_json['diagnosis']
        self.assertIsInstance(diagnosis, dict)
        self.assertIn('condition_name', diagnosis)
        self.assertIn('probability', diagnosis)
        self.assertEqual(diagnosis['condition_name'], 'Myocardial Infarction')
        self.assertGreater(diagnosis['probability'], 0.0)
        self.assertEqual(response_json['status'], 'success')

    def test_upload_ecg_file(self):
        data = io.BytesIO(b'Sample ECG file data')
        data.seek(0)
        response = self.app.post(
            '/api/ecg/upload',
            data={'file': (data, 'test_ecg.mat')},
            content_type='multipart/form-data'
        )
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        self.assertIn('success', response_json)
        self.assertIn('message', response_json)
        self.assertIn('file_id', response_json)
        self.assertTrue(response_json['success'])
        self.assertEqual(response_json['message'], 'File uploaded successfully.')

    def test_process_ecg_file(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        request_data = {"file_id": "sample_file_id"}
        response = self.app.post('/api/ecg/process', json=request_data, headers=headers)
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        expected_keys = ['success', 'message', 'process_id']
        for key in expected_keys:
            self.assertIn(key, response_json)
        self.assertEqual(response_json['success'], True)
        self.assertEqual(response_json['message'], 'Processing started.')
        self.assertEqual(response_json['process_id'], 'sample_process_id')
