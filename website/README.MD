# Project Name: Smartify

## Overview

Smartify is a comprehensive solution for managing and predicting health-related data using machine learning. The application includes user authentication, role-based access, and machine learning predictions for health conditions. It supports Google OAuth2 login, email verification, and integrates with several machine learning models to provide predictions.

## Features

- **User Authentication**: Register, login, and verify accounts using email and Google OAuth2.
- **Role-Based Access**: Different pages and functionalities based on user roles.
- **Machine Learning Predictions**: Predict health conditions using various machine learning models.
- **Beautiful UI**: Responsive and modern design using Tailwind CSS.
- **Email Verification**: Secure account verification via email.

## Prerequisites

- Python 3.7+
- Flask
- SQLite
- scikit-learn
- joblib
- pandas
- Google OAuth2 credentials
- SMTP server details for email

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use 
   `venv\Scripts\activate`

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt

4. **Set up environment variables:**

   ```bash
    SECRET_KEY=your_secret_key
    SECURITY_PASSWORD_SALT=your_password_salt
    GOOGLE_CLIENT_ID=your_google_client_id
    GOOGLE_CLIENT_SECRET=your_google_client_secret
    SMTP_SERVER=smtp.gmail.com
    SMTP_PORT=587
    SMTP_USERNAME=your_email@gmail.com
    SMTP_PASSWORD=your_email_password


# Usage

1. Run the application:
    ```bash
    python app.py

2. Navigate to the application:

   Open your web browser and go to http://localhost:5000.

### Endpoints
- /: Home page
- /home: Home page
- /register: User registration
- /verify: Email verification
- /login: User login
- /google_login: Google OAuth2 login
- /google_callback: Google OAuth2 callback
- /dashboard: User dashboard
- /admin_page: Admin page
- /provider_page: Healthcare provider page
- /user_page: User page
- /logout: User logout
- /predict: Machine learning prediction endpoint


### Machine Learning

The application uses the following machine learning models:

- Logistic Regression
- SVM
- Decision Tree
- Random Forest
- KNN

Models and scalers are loaded from static/models/.


Contributing
Contributions are welcome! Please follow these steps:

- Fork the repository.
- Create a feature branch.
- Commit your changes.
- Push to the branch.
- Create a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

Flask
scikit-learn
Tailwind CSS
Google OAuth2
For any issues or feature requests, please open an issue on GitHub.