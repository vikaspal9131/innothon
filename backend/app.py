from flask import Flask, request, jsonify, send_file, abort, send_from_directory
from werkzeug.utils import secure_filename
import os
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mat'}
app.config['IMAGE_FOLDER'] = 'images'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Helper function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# User Management
@app.route('/api/users/register', methods=['POST'])
def register_user():
    data = request.json
    # Handle user registration logic
    # Here you would normally store the user details in a database
    return jsonify({"success": True, "message": "User registered successfully."})

@app.route('/api/users/login', methods=['POST'])
def login_user():
    data = request.json
    # Handle user login logic
    # Validate user credentials and generate token
    return jsonify({"success": True, "token": "sample_token"})

@app.route('/api/users/profile', methods=['GET'])
def get_user_profile():
    token = request.headers.get('Authorization')
    # Handle getting user profile logic
    # Use the token to fetch user data from a database
    return jsonify({"username": "sample_user", "email": "user@example.com", "profile_data": {}})

@app.route('/api/users/profile', methods=['PUT'])
def update_user_profile():
    token = request.headers.get('Authorization')
    data = request.json
    # Handle updating user profile logic
    return jsonify({"success": True, "message": "Profile updated successfully."})

@app.route('/api/users/password', methods=['PUT'])
def change_password():
    token = request.headers.get('Authorization')
    data = request.json
    # Handle changing password logic
    return jsonify({"success": True, "message": "Password changed successfully."})

# ECG Management
@app.route('/api/ecg/upload', methods=['POST'])
def upload_ecg_file():
    if 'file' not in request.files:
        return jsonify({"success": False, "message": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"success": False, "message": "No selected file"})
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({"success": True, "message": "File uploaded successfully.", "file_id": filename})
    return jsonify({"success": False, "message": "Invalid file type"})

@app.route('/api/ecg/process', methods=['POST'])
def process_ecg_file():
    data = request.json
    file_id = data.get('file_id')
    # Handle ECG processing logic
    # Process the file and return a process ID
    return jsonify({"success": True, "message": "Processing started.", "process_id": "sample_process_id"})

@app.route('/api/ecg/diagnosis/<file_id>', methods=['GET'])
def get_ecg_diagnosis(file_id):
    # Handle getting ECG diagnosis
    ECG_DIAGNOSES = {
    "example_file_id": {
            "condition_name": "Myocardial Infarction",
            "probability": 0.95,
            "details": {
                "description": "Acute myocardial infarction (MI) is a condition where blood flow to the heart muscle is obstructed.",
                "treatment": "Immediate medical treatment including medications and potential surgical interventions."
            }
        }
    }
    diagnosis = ECG_DIAGNOSES.get(file_id)
    
    if diagnosis:
        response = {
            "diagnosis": diagnosis,
            "status": "success"
        }
        return jsonify(response)
    else:
        response = {
            "diagnosis": {},
            "status": "error",
            "message": "Diagnosis not found for the provided file ID."
        }
        return jsonify(response), 404

@app.route('/api/ecg/report/<file_id>', methods=['GET'])
def download_ecg_report(file_id):
    report_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{file_id}.pdf")
    if os.path.exists(report_path):
        return send_file(report_path, as_attachment=True)
    return jsonify({"success": False, "message": "Report not found"})

# Diagnosis Information
@app.route('/api/diagnosis/<diagnosis_id>', methods=['GET'])
def get_diagnosis_info(diagnosis_id):
    DIAGNOSIS_DATABASE = {
    "1234": {
            "diagnosis_id": "1234",
            "condition_name": "Myocardial Infarction",
            "description": "A condition where blood flow to the heart is blocked.",
        },
        "5678": {
            "diagnosis_id": "5678",
            "condition_name": "Heart Failure",
            "description": "A condition where the heart is unable to pump enough blood.",
        },
    }

    # Fetch diagnosis details based on diagnosis ID
    diagnosis_info = DIAGNOSIS_DATABASE.get(diagnosis_id)
    
    if diagnosis_info is None:
        # If diagnosis_id is not found, return 404 Not Found
        abort(404, description=f"Diagnosis with ID {diagnosis_id} not found.")
    
    return jsonify(diagnosis_info)


@app.route('/api/diagnosis', methods=['GET'])
def list_all_diagnoses():
    # Handle listing all diagnoses
    return jsonify([
        {"diagnosis_id": "sample_id", "condition_name": "Condition A", "description": "Description of Condition A"},
        {"diagnosis_id": "sample_id_2", "condition_name": "Condition B", "description": "Description of Condition B"}
    ])

@app.route('/api/ecg/images', methods=['GET'])
def get_ecg_images():
    try:
        # List all files in the IMAGE_FOLDER
        images = os.listdir(app.config['IMAGE_FOLDER'])
        # Filter to include only image files (you can adjust this filter as needed)
        image_files = [file for file in images if file.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        
        # Create a list of image details
        image_list = []
        for image in image_files:
            image_list.append({
                "image_name": image,
                "image_url": f"http://localhost:5000/images/{image}"  # URL to access the image
            })
        
        return jsonify(image_list)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/images/<filename>')
def serve_image(filename):
    try:
        # Check if the requested file exists in the IMAGE_FOLDER
        if not os.path.isfile(os.path.join(app.config['IMAGE_FOLDER'], filename)):
            return jsonify({"error": "File not found"}), 404
        
        # Serve the image file from the directory
        return send_from_directory('../images', filename)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Model Information
@app.route('/api/model', methods=['GET'])
def get_model_details():
    try:
        # Define the path to the model_info.json file
        file_path = 'modelPerformance/model_info_resnet50_E10.json'
        
        # Ensure the file exists
        if not os.path.isfile(file_path):
            return jsonify({"error": "Model information file not found"}), 404
        
        # Read the model information from the file
        with open(file_path, 'r') as file:
            model_info = json.load(file)
        
        # Return the model details as JSON
        return jsonify(model_info)
    
    except Exception as e:
        return jsonify({'error':str(e)}),500

@app.route('/api/model/metrics', methods=['GET'])
def get_model_performance_metrics():
    # Read model performance metrics from a JSON file
    try:
        with open('modelPerformance/model_metrics_resnet50_E10.json', 'r') as file:
            metrics = json.load(file)
    except FileNotFoundError:
        return jsonify({"error": "Metrics file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding metrics file"}), 500

    return jsonify(metrics)

# Project Information
@app.route('/api/project', methods=['GET'])
def get_project_details():
    """
    Handle fetching project details.
    This endpoint provides information about the project, including its name, version, description, and more.

    Returns:
        JSON: A dictionary containing project details.
    """
    project_details = {
        "project_name": "ECG Signal Diagnosis",
        "version": "1.0",
        "description": "A project to diagnose ECG signals using machine learning.",
        "author": "Code Esper",
        "date_created": "2024-08-27",
        "last_updated": "2024-08-27",
        "technologies_used": [
            "Flask",
            "Python",
            "Machine Learning",
            "ECG Signal Processing",
            "TensorFlow",
            "Keras"
        ],
        "features": [
            "ECG Signal Upload",
            "Real-Time Signal Processing",
            "Disease Diagnosis",
            "Detailed Reports",
            "Performance Metrics"
        ],
        "api_endpoints": {
            "/api/ecg/upload": "Upload ECG signal files.",
            "/api/ecg/process": "Process the uploaded ECG file.",
            "/api/ecg/diagnosis/{file_id}": "Retrieve diagnosis results for a specific ECG file.",
            "/api/ecg/report/{file_id}": "Generate a detailed report for a specific ECG file.",
            "/api/diagnosis/{diagnosis_id}": "Retrieve diagnosis details using the diagnosis ID.",
            "/api/model": "Get information about the current ECG analysis model.",
            "/api/model/metrics": "Get performance metrics of the current ECG analysis model.",
            "/api/project": "Get project information."
        }
    }
    return jsonify(project_details)

@app.route('/api/project/docs', methods=['GET'])
def get_project_documentation():
    """
    API endpoint to fetch the project documentation URL.
    """
    # Sample data representing the project documentation
    documentation = {
        "title": "ECG Analysis API Documentation",
        "description": "This API provides endpoints for uploading, processing, diagnosing, and retrieving reports of ECG signals.",
        "endpoints": [
            {
                "endpoint": "/api/users/register",
                "method": "POST",
                "description": "Register a new user.",
                "parameters": {
                    "email": "string (required)",
                    "password": "string (required)"
                }
            },
            {
                "endpoint": "/api/users/login",
                "method": "POST",
                "description": "Login with an existing user account.",
                "parameters": {
                    "email": "string (required)",
                    "password": "string (required)"
                }
            },
            {
                "endpoint": "/api/ecg/upload",
                "method": "POST",
                "description": "Upload an ECG file for processing.",
                "parameters": {
                    "file": "file (required)",
                    "Authorization": "string (required)"
                }
            },
            {
                "endpoint": "/api/ecg/process",
                "method": "POST",
                "description": "Process the uploaded ECG file.",
                "parameters": {
                    "file_id": "string (required)",
                    "Authorization": "string (required)"
                }
            },
            {
                "endpoint": "/api/ecg/diagnosis/{file_id}",
                "method": "GET",
                "description": "Get the diagnosis results for a specific ECG file.",
                "parameters": {
                    "file_id": "string (required)",
                    "Authorization": "string (required)"
                }
            },
            {
                "endpoint": "/api/ecg/report/{file_id}",
                "method": "GET",
                "description": "Generate a detailed report for a specific ECG file.",
                "parameters": {
                    "file_id": "string (required)",
                    "Authorization": "string (required)"
                }
            },
            {
                "endpoint": "/api/diagnosis/{diagnosis_id}",
                "method": "GET",
                "description": "Retrieve diagnosis details using the diagnosis ID.",
                "parameters": {
                    "diagnosis_id": "string (required)",
                    "Authorization": "string (required)"
                }
            },
            {
                "endpoint": "/api/model",
                "method": "GET",
                "description": "Get information about the current model used for ECG analysis.",
                "parameters": {
                    "Authorization": "string (required)"
                }
            },
            {
                "endpoint": "/api/model/metrics",
                "method": "GET",
                "description": "Get the performance metrics of the current ECG analysis model.",
                "parameters": {
                    "Authorization": "string (required)"
                }
            }
        ]
    }
    try:
        
        # Create the response JSON
        response = {
            "success": True,
            "documentation": documentation 
        }
        
        # Return the response with a status code 200
        return jsonify(response), 200

    except Exception as e:
        # In case of any error, return an error message with status code 500
        return jsonify({
            "success": False,
            "error": "An error occurred while fetching the documentation.",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5050)
