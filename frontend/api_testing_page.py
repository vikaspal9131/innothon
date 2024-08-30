import streamlit as st
import requests

def api_testing_page():
    st.title("🔍 API Testing")

    st.write(
        """
        ## Test API Endpoints
        Use this page to test various API endpoints by providing the required input and checking the response.
        """
    )

    # User selects the API endpoint to test
    st.subheader("Select an API Endpoint")
    endpoint = st.selectbox("API Endpoint", [
        "/api/users/register",
        "/api/users/login",
        "/api/users/profile",
        "/api/users/password",
        "/api/ecg/upload",
        "/api/ecg/process",
        "/api/ecg/diagnosis/{file_id}",
        "/api/ecg/report/{file_id}",
        "/api/diagnosis/{diagnosis_id}",
        "/api/model",
        "/api/model/metrics",
        "/api/project",
        "/api/project/docs"
    ])

    # Input fields with descriptions for the selected endpoint
    if endpoint == "/api/users/register":
        st.write("**Description:** Register a new user.")
        st.write("**Parameters:**")
        st.write("- **username (string):** The desired username for the new user.")
        st.write("- **password (string):** The password for the new user. Must be strong.")
        st.write("- **email (string):** The email address of the new user.")
        st.write("**Example:**")
        st.json({
            "username": "john_doe",
            "password": "securePass123",
            "email": "john@example.com"
        })
        
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")
        if st.button("Submit"):
            response = requests.post("http://localhost:5000/api/users/register", json={
                "username": username,
                "password": password,
                "email": email
            })
            st.json(response.json())

    elif endpoint == "/api/users/login":
        st.write("**Description:** Log in an existing user.")
        st.write("**Parameters:**")
        st.write("- **username (string):** The username of the user.")
        st.write("- **password (string):** The password of the user.")
        st.write("**Example:**")
        st.json({
            "username": "john_doe",
            "password": "securePass123"
        })
        
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Submit"):
            response = requests.post("http://localhost:5000/api/users/login", json={
                "username": username,
                "password": password
            })
            st.json(response.json())

    elif endpoint == "/api/users/profile":
        st.write("**Description:** Retrieve the profile of the logged-in user.")
        st.write("**Parameters:**")
        st.write("- **Authorization Token (string):** A valid JWT token obtained after login.")
        st.write("**Example:**")
        st.write("Authorization: Bearer `<your_token_here>`")
        
        token = st.text_input("Authorization Token")
        if st.button("Submit"):
            response = requests.get("http://localhost:5000/api/users/profile", headers={
                "Authorization": f"Bearer {token}"
            })
            st.json(response.json())

    elif endpoint == "/api/users/password":
        st.write("**Description:** Change the password of the logged-in user.")
        st.write("**Parameters:**")
        st.write("- **Authorization Token (string):** A valid JWT token obtained after login.")
        st.write("- **old_password (string):** The current password of the user.")
        st.write("- **new_password (string):** The new password to be set.")
        st.write("**Example:**")
        st.json({
            "old_password": "securePass123",
            "new_password": "newSecurePass456"
        })
        
        token = st.text_input("Authorization Token")
        old_password = st.text_input("Old Password", type="password")
        new_password = st.text_input("New Password", type="password")
        if st.button("Submit"):
            response = requests.put("http://localhost:5000/api/users/password", headers={
                "Authorization": f"Bearer {token}"
            }, json={
                "old_password": old_password,
                "new_password": new_password
            })
            st.json(response.json())

    elif endpoint == "/api/ecg/upload":
        st.write("**Description:** Upload an ECG file.")
        st.write("**Parameters:**")
        st.write("- **Authorization Token (string):** A valid JWT token obtained after login.")
        st.write("- **file (file):** The ECG file in `.mat` format.")
        st.write("**Example:**")
        st.write("Upload an ECG file named `ecg_sample.mat`.")
        
        token = st.text_input("Authorization Token")
        uploaded_file = st.file_uploader("Choose an ECG file", type=["mat"])
        if st.button("Submit"):
            files = {'file': uploaded_file}
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.post("http://localhost:5000/api/ecg/upload", headers=headers, files=files)
            st.json(response.json())

    elif endpoint == "/api/ecg/process":
        st.write("**Description:** Process the uploaded ECG file.")
        st.write("**Parameters:**")
        st.write("- **Authorization Token (string):** A valid JWT token obtained after login.")
        st.write("- **file_id (string):** The ID of the uploaded ECG file to be processed.")
        st.write("**Example:**")
        st.json({
            "file_id": "1234567890abcdef"
        })

        token = st.text_input("Authorization Token")
        file_id = st.text_input("File ID")
        if st.button("Submit"):
            response = requests.post(f"http://localhost:5000/api/ecg/process", headers={
                "Authorization": f"Bearer {token}"
            }, json={
                "file_id": file_id
            })
            st.json(response.json())

    elif endpoint == "/api/ecg/diagnosis/{file_id}":
        st.write("**Description:** Get the diagnosis results for a specific ECG file.")
        st.write("**Parameters:**")
        st.write("- **Authorization Token (string):** A valid JWT token obtained after login.")
        st.write("- **file_id (string):** The ID of the processed ECG file for diagnosis.")
        st.write("**Example:**")
        st.json({
            "file_id": "1234567890abcdef"
        })

        token = st.text_input("Authorization Token")
        file_id = st.text_input("File ID")
        if st.button("Submit"):
            response = requests.get(f"http://localhost:5000/api/ecg/diagnosis/{file_id}", headers={
                "Authorization": f"Bearer {token}"
            })
            st.json(response.json())

    elif endpoint == "/api/ecg/report/{file_id}":
        st.write("**Description:** Generate a detailed report for a specific ECG file.")
        st.write("**Parameters:**")
        st.write("- **Authorization Token (string):** A valid JWT token obtained after login.")
        st.write("- **file_id (string):** The ID of the ECG file for which the report is to be generated.")
        st.write("**Example:**")
        st.json({
            "file_id": "1234567890abcdef"
        })

        token = st.text_input("Authorization Token")
        file_id = st.text_input("File ID")
        if st.button("Submit"):
            response = requests.get(f"http://localhost:5000/api/ecg/report/{file_id}", headers={
                "Authorization": f"Bearer {token}"
            })
            st.json(response.json())

    elif endpoint == "/api/diagnosis/{diagnosis_id}":
        st.write("**Description:** Retrieve diagnosis details using the diagnosis ID.")
        st.write("**Parameters:**")
        st.write("- **Authorization Token (string):** A valid JWT token obtained after login.")
        st.write("- **diagnosis_id (string):** The ID of the diagnosis to be retrieved.")
        st.write("**Example:**")
        st.json({
            "diagnosis_id": "abcdef1234567890"
        })

        token = st.text_input("Authorization Token")
        diagnosis_id = st.text_input("Diagnosis ID")
        if st.button("Submit"):
            response = requests.get(f"http://localhost:5000/api/diagnosis/{diagnosis_id}", headers={
                "Authorization": f"Bearer {token}"
            })
            st.json(response.json())

    elif endpoint == "/api/model":
        st.write("**Description:** Get information about the current model used for ECG analysis.")
        st.write("**Parameters:**")
        st.write("- **Authorization Token (string):** A valid JWT token obtained after login.")
        st.write("**Example:**")
        st.write("No additional parameters are required.")

        token = st.text_input("Authorization Token")
        if st.button("Submit"):
            response = requests.get(f"http://localhost:5000/api/model", headers={
                "Authorization": f"Bearer {token}"
            })
            st.json(response.json())

    elif endpoint == "/api/model/metrics":
        st.write("**Description:** Get the performance metrics of the current ECG analysis model.")
        st.write("**Parameters:**")
        st.write("- **Authorization Token (string):** A valid JWT token obtained after login.")
        st.write("**Example:**")
        st.write("No additional parameters are required.")

        token = st.text_input("Authorization Token")
        if st.button("Submit"):
            response = requests.get(f"http://localhost:5000/api/model/metrics", headers={
                "Authorization": f"Bearer {token}"
            })
            st.json(response.json())

    # Handle the /api/project endpoint
    elif endpoint == "/api/project":
        st.write("**Description:** Retrieve information about the project, including its name, version, description, and other relevant details.")
        st.write("**Parameters:**")
        st.write("No parameters are required for this endpoint.")

        if st.button("Submit"):
            response = requests.get(f"http://localhost:5000/api/project")
            st.json(response.json())
            
    elif endpoint == "/api/project/docs":
        st.write("**Description:** Retrieve the documentation content of the project.")
        st.write("**Parameters:**")
        st.write("No parameters are required for this endpoint.")

        if st.button("Submit"):
            response = requests.get("http://localhost:5000/api/project/docs")
            st.write("**Documentation Content:**")
            st.json(response.json())
    # Continue similarly for other endpoints...

    else:
        st.write("Select an endpoint to test.")

