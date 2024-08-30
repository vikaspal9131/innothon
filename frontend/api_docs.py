import streamlit as st

def show_api_docs():
    # Streamlit Page Title
    st.title("📜 API Documentation")

    st.write(
        """
        ## Overview
        Welcome to the API documentation for the ECG Signal Diagnosis project. Below you'll find details on the available API endpoints, including their usage, parameters, and responses.
        """
    )

    # User Management
    st.header("👤 User Management")

    st.subheader("1. User Registration")
    st.write("**Endpoint:** `POST /api/users/register`")
    st.write("**Request Body:**")
    st.json({
        "username": "string",
        "password": "string",
        "email": "string"
    })
    st.write("**Response:**")
    st.json({
        "success": True,
        "message": "User registered successfully."
    })

    st.subheader("2. User Login")
    st.write("**Endpoint:** `POST /api/users/login`")
    st.write("**Request Body:**")
    st.json({
        "username": "string",
        "password": "string"
    })
    st.write("**Response:**")
    st.json({
        "success": True,
        "token": "string"
    })

    st.subheader("3. User Profile")
    st.write("**Endpoint:** `GET /api/users/profile`")
    st.write("**Headers:** `Authorization: Bearer <token>`")
    st.write("**Response:**")
    st.json({
        "username": "string",
        "email": "string",
        "profile_data": { ... }
    })

    st.subheader("4. Update User Profile")
    st.write("**Endpoint:** `PUT /api/users/profile`")
    st.write("**Headers:** `Authorization: Bearer <token>`")
    st.write("**Request Body:**")
    st.json({
        "email": "string",
        "profile_data": { ... }
    })
    st.write("**Response:**")
    st.json({
        "success": True,
        "message": "Profile updated successfully."
    })

    st.subheader("5. Change Password")
    st.write("**Endpoint:** `PUT /api/users/password`")
    st.write("**Headers:** `Authorization: Bearer <token>`")
    st.write("**Request Body:**")
    st.json({
        "old_password": "string",
        "new_password": "string"
    })
    st.write("**Response:**")
    st.json({
        "success": True,
        "message": "Password changed successfully."
    })

    # ECG Management
    st.header("📊 ECG Management")

    st.subheader("1. Upload ECG File")
    st.write("**Endpoint:** `POST /api/ecg/upload`")
    st.write("**Headers:** `Authorization: Bearer <token>`")
    st.write("**Form Data:**")
    st.json({
        "file": "<file>"
    })
    st.write("**Response:**")
    st.json({
        "success": True,
        "message": "File uploaded successfully.",
        "file_id": "string"
    })

    st.subheader("2. Process ECG File")
    st.write("**Endpoint:** `POST /api/ecg/process`")
    st.write("**Headers:** `Authorization: Bearer <token>`")
    st.write("**Request Body:**")
    st.json({
        "file_id": "string"
    })
    st.write("**Response:**")
    st.json({
        "success": True,
        "message": "Processing started.",
        "process_id": "string"
    })

    st.subheader("3. Get ECG Diagnosis")
    st.write("**Endpoint:** `GET /api/ecg/diagnosis/{file_id}`")
    st.write("**Headers:** `Authorization: Bearer <token>`")
    st.write("**Response:**")
    st.json({
        "diagnosis": { ... },
        "status": "string"
    })

    st.subheader("4. Download ECG Report")
    st.write("**Endpoint:** `GET /api/ecg/report/{file_id}`")
    st.write("**Headers:** `Authorization: Bearer <token>`")
    st.write("**Response:**")
    st.json({
        "report_url": "string"
    })

    # Diagnosis Information
    st.header("🩺 Diagnosis Information")

    st.subheader("1. Get Diagnosis Information")
    st.write("**Endpoint:** `GET /api/diagnosis/{diagnosis_id}`")
    st.write("**Response:**")
    st.json({
        "diagnosis": { ... }
    })

    st.subheader("2. List All Diagnoses")
    st.write("**Endpoint:** `GET /api/diagnosis`")
    st.write("**Response:**")
    st.json([
        { "diagnosis_id": "string", "condition_name": "string", "description": "string" },
        ...
    ])

    st.subheader("3. Get ECG Images")
    st.write("**Endpoint:** `GET /api/ecg/images`")
    st.write("**Response:**")
    st.json([
        { "image_name": "string", "image_url": "string" },
        ...
    ])

    # Model Information
    st.header("🤖 Model Information")

    st.subheader("1. Get Model Details")
    st.write("**Endpoint:** `GET /api/model`")
    st.write("**Response:**")
    st.json({
        "model_version": "string",
        "description": "string",
        "last_update": "date"
    })

    st.subheader("2. Get Model Performance Metrics")
    st.write("**Endpoint:** `GET /api/model/metrics`")
    st.write("**Response:**")
    st.json({
        "accuracy": "float",
        "precision": "float",
        "recall": "float",
        "f1_score": "float"
    })

    # Project Information
    st.header("🛠️ Project Information")

    st.subheader("1. Get Project Details")
    st.write("**Endpoint:** `GET /api/project`")
    st.write("**Response:**")
    st.json({
        "project_name": "string",
        "version": "string",
        "description": "string"
    })

    st.subheader("2. Get Project Documentation")
    st.write("**Endpoint:** `GET /api/project/docs`")
    st.write("**Response:**")
    st.json({
        "documentation_url": "string"
    })

    # FAQ
    st.header("❓ FAQ")

    st.subheader("1. What is the purpose of the ECG Signal Diagnosis project?")
    st.write("The ECG Signal Diagnosis project aims to analyze ECG signals and diagnose potential cardiac conditions using machine learning models.")

    st.subheader("2. How do I use the API?")
    st.write("To use the API, you need to authenticate using your user credentials. You can then upload ECG files, process them, and retrieve diagnosis information through the available endpoints.")

    st.subheader("3. What type of data do I need to provide for diagnosis?")
    st.write("You need to upload an ECG signal file in `.mat` format. The file will be processed to provide diagnosis information.")

    st.subheader("4. How is the diagnosis made?")
    st.write("The ECG signals are processed using a trained deep learning model that analyzes the data and provides diagnosis based on predefined conditions.")

    st.subheader("5. Can I download the reports?")
    st.write("Yes, you can download detailed ECG reports after the processing is complete using the provided endpoints.")

    st.subheader("6. How can I get help if I encounter issues?")
    st.write("You can contact support through the `POST /api/support/contact` endpoint to submit your issues or queries.")

    # Additional Information
    st.header("ℹ️ Additional Information")

    st.write(
        """
        If you have any other questions or need further assistance, please refer to the project documentation or contact our support team.
        """
    )
