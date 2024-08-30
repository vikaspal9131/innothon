import unittest
from backend.app import app
import io
import json

class ProjectApiTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the Flask test client
        self.app = app.test_client()
        self.app.testing = True
        self.token = "your_test_auth_token"

    def test_get_project_details(self):
        # Send a GET request to the /api/project endpoint
        response = self.app.get('/api/project')
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the response JSON contains the expected keys
        expected_keys = ['project_name', 'version', 'description']
        response_json = response.get_json()
        for key in expected_keys:
            self.assertIn(key, response_json)
        # Check the values if needed
        self.assertEqual(response_json['project_name'], 'ECG Signal Diagnosis')
        self.assertEqual(response_json['version'], '1.0')
        self.assertEqual(response_json['description'], 'A project to diagnose ECG signals using machine learning')

    def test_get_project_docs(self):
        # Send a GET request to the /api/project/docs endpoint
        response = self.app.get('/api/project/docs')
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the response JSON contains the expected keys
        expected_keys = ['documentation_url']
        response_json = response.get_json()
        for key in expected_keys:
            self.assertIn(key, response_json)
        # Check the value if needed
        self.assertEqual(response_json['documentation_url'], 'http://example.com/docs')

    def test_get_model_metrics(self):
        # Send a GET request to the /api/model/metrics endpoint
        response = self.app.get('/api/model/metrics')
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the response JSON contains the expected keys
        expected_keys = ['accuracy', 'precision', 'recall', 'f1_score']
        response_json = response.get_json()
        for key in expected_keys:
            self.assertIn(key, response_json)
        # Check the values if needed
        self.assertTrue(isinstance(response_json['accuracy'], (int, float)))
        self.assertTrue(isinstance(response_json['precision'], (int, float)))
        self.assertTrue(isinstance(response_json['recall'], (int, float)))
        self.assertTrue(isinstance(response_json['f1_score'], (int, float)))

    def test_get_model_details(self):
        # Send a GET request to the /api/model endpoint
        response = self.app.get('/api/model')
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the response JSON contains the expected keys
        expected_keys = ['model_version', 'description', 'last_update']
        response_json = response.get_json()
        for key in expected_keys:
            self.assertIn(key, response_json)
        # Check the values if needed
        self.assertEqual(response_json['model_version'], '1.0')
        self.assertEqual(response_json['description'], 'Description of the model')
        self.assertIn('last_update', response_json)  # Assuming last_update is a date or timestamp

    def test_get_ecg_images(self):
        # Send a GET request to the /api/ecg/images endpoint
        response = self.app.get('/api/ecg/images')
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the response JSON contains the expected structure
        response_json = response.get_json()
        self.assertIsInstance(response_json, list)
        
        # Define expected structure for the response
        expected_images = [
            {"image_name": "image1.png", "image_url": "http://example.com/image1.png"},
            {"image_name": "image2.png", "image_url": "http://example.com/image2.png"}
        ]

        # Check if the response JSON matches the expected images
        self.assertEqual(response_json, expected_images)

    def test_list_all_diagnoses(self):
        # Send a GET request to the /api/diagnosis endpoint
        response = self.app.get('/api/diagnosis')
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the response JSON is a list
        response_json = response.get_json()
        self.assertIsInstance(response_json, list)
        
        # Optionally, check if the list contains at least one item and the expected structure
        if len(response_json) > 0:
            first_item = response_json[0]
            self.assertIn('diagnosis_id', first_item)
            self.assertIn('condition_name', first_item)
            self.assertIn('description', first_item)
            # Optionally, check values
            self.assertIsInstance(first_item['diagnosis_id'], str)
            self.assertIsInstance(first_item['condition_name'], str)
            self.assertIsInstance(first_item['description'], str)

    def test_get_diagnosis_information(self):
        # Example diagnosis ID to test
        diagnosis_id = '1234'

        # Send a GET request to the /api/diagnosis/{diagnosis_id} endpoint
        response = self.app.get(f'/api/diagnosis/{diagnosis_id}')
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the response JSON contains the expected structure
        response_json = response.get_json()
        self.assertIn('diagnosis_id', response_json)
        self.assertIn('condition_name', response_json)
        self.assertIn('description', response_json)
        
        # Optionally, you can assert the values returned
        self.assertEqual(response_json['diagnosis_id'], diagnosis_id)
        self.assertEqual(response_json['condition_name'], 'Myocardial Infarction')  # Replace with actual expected value
        self.assertEqual(response_json['description'], 'A condition where blood flow to the heart is blocked.')  # Replace with actual expected value

    def test_get_ecg_report(self):
        pass

    def test_get_ecg_diagnosis(self):
        # Replace with a valid file_id for testing
        file_id = "example_file_id"

        # Send a GET request to the /api/ecg/diagnosis/<file_id> endpoint
        response = self.app.get(f'/api/ecg/diagnosis/{file_id}', headers={
            'Authorization': f'Bearer {self.token}'  # Include the authorization header if needed
        })

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response JSON contains the expected keys
        expected_keys = ['diagnosis', 'status']
        response_json = response.get_json()
        for key in expected_keys:
            self.assertIn(key, response_json)

        # Check the structure and content of the diagnosis data
        # Adjust based on the actual response structure and content
        diagnosis = response_json['diagnosis']
        self.assertIsInstance(diagnosis, dict)  # Ensure that the diagnosis is a dictionary

        # Example checks, adjust based on your actual data
        self.assertIn('condition_name', diagnosis)
        self.assertIn('probability', diagnosis)

        # Example values, replace with appropriate expected values
        self.assertEqual(diagnosis['condition_name'], 'Myocardial Infarction')
        self.assertGreater(diagnosis['probability'], 0.0)

        # Optionally, check the status field
        self.assertEqual(response_json['status'], 'success')

    def test_process_ecg_file(self):
        # Simulate authentication token (you need to replace 'your_token' with an actual token if required)
        headers = {
            'Authorization': 'Bearer your_token'
        }
        
        # Data for the POST request
        request_data = {
            "file_id": "sample_file_id"
        }
        
        # Send a POST request to the /api/ecg/process endpoint
        response = self.app.post('/api/ecg/process', json=request_data, headers=headers)
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the response JSON contains the expected keys
        expected_keys = ['success', 'message', 'process_id']
        response_json = response.get_json()
        for key in expected_keys:
            self.assertIn(key, response_json)
        
        # Optionally check the values in the response
        self.assertEqual(response_json['success'], True)
        self.assertEqual(response_json['message'], 'Processing started.')
        self.assertEqual(response_json['process_id'], 'sample_process_id')

    def test_upload_ecg_file(self):
        # Create a sample file-like object
        data = io.BytesIO(b'Sample ECG file data')
        data.seek(0)
        
        # Send a POST request with the file
        response = self.app.post(
            '/api/ecg/upload',
            data={'file': (data, 'test_ecg.mat')},
            content_type='multipart/form-data'
        )
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the response JSON contains the expected keys
        response_json = response.get_json()
        self.assertIn('success', response_json)
        self.assertIn('message', response_json)
        self.assertIn('file_id', response_json)
        
        # Optionally, verify the content of the response
        self.assertTrue(response_json['success'])
        self.assertEqual(response_json['message'], 'File uploaded successfully.')

    def test_register_user(self):
        # Sample request body for user registration
        request_body = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com"
        }

        # Send a POST request to the /api/users/register endpoint
        response = self.app.post('/api/users/register', 
                                 data=json.dumps(request_body), 
                                 content_type='application/json')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the response JSON contains the success key
        response_json = response.get_json()
        self.assertIn('success', response_json)
        self.assertIn('message', response_json)
        self.assertTrue(response_json['success'])
        self.assertEqual(response_json['message'], 'User registered successfully.')

    def test_user_login(self):
        # Sample user credentials for testing
        login_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }

        # Send a POST request to the /api/users/login endpoint
        response = self.app.post('/api/users/login', json=login_data)
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response JSON contains the expected keys
        response_json = response.get_json()
        self.assertIn('success', response_json)
        self.assertIn('token', response_json)

        # Check the success status
        self.assertTrue(response_json['success'])
        self.assertIsInstance(response_json['token'], str)

    def test_get_user_profile(self):
        # Send a GET request to the /api/users/profile endpoint with the authorization token
        response = self.app.get(
            '/api/users/profile',
            headers={'Authorization': f'Bearer {self.token}'}
        )
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the response JSON contains the expected keys
        expected_keys = ['username', 'email', 'profile_data']
        response_json = response.get_json()
        for key in expected_keys:
            self.assertIn(key, response_json)
        # Check the values if needed
        self.assertEqual(response_json['username'], 'sample_user')
        self.assertEqual(response_json['email'], 'user@example.com')
        self.assertEqual(response_json['profile_data'], {})

if __name__ == '__main__':
    unittest.main()