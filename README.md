Credit Card Fraud Detection Web Application
This project provides a simple, user-friendly web interface for a credit card fraud detection model. Users can input various transaction features, and the application will predict whether the transaction is legitimate or fraudulent in real-time.

Features
Interactive Web Interface: A clean and responsive web form built with HTML, CSS, and JavaScript.

Real-time Prediction: Utilizes a pre-trained Logistic Regression model to classify transactions as legitimate or fraudulent.

Asynchronous Communication: Uses Flask as a backend API to handle predictions without full page reloads, providing a smooth user experience.

Clear Feedback: Displays prediction results with distinct visual cues (colors) for easy interpretation.

Loading Indicator: A spinner indicates when a prediction is being processed.

Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.x

pip (Python package installer, usually comes with Python)

Installation
Follow these steps to set up and run the application locally:

1. Create Project Directory
Create a new directory for your project and navigate into it:

mkdir credit_card_fraud_app
cd credit_card_fraud_app

Inside credit_card_fraud_app, create a sub-directory named templates:

mkdir templates

2. Save Your Trained Model
You need to save your trained Logistic Regression model from your Jupyter Notebook (or Python script) as a .pkl file. Ensure this file is placed directly in the credit_card_fraud_app directory (next to app.py).

If you haven't already, run the following code in your model training environment to save your model object:

import pickle
# Assuming 'model' is your trained LogisticRegression object
with open('credit_card_fraud_model.pkl', 'wb') as file:
    pickle.dump(model, file)

5. Install Python Dependencies
Open your terminal or command prompt, navigate to the credit_card_fraud_app directory, and install the required Python libraries:

pip install Flask pandas scikit-learn

Usage
To run the application:

Open your terminal or command prompt.

Navigate to the credit_card_fraud_app directory.

Run the Flask application:

python app.py

Open your web browser and go to the address displayed in your terminal (usually http://127.0.0.1:5000/).

You will see the Credit Card Fraud Detection Dashboard. Enter the required 30 feature values into the input fields and click the "Predict Fraud" button. The prediction result will appear on the right side of the dashboard.

Project Structure
credit_card_fraud_app/
├── app.py                      # Flask application backend logic
├── credit_card_fraud_model.pkl # The pre-trained machine learning model
└── templates/
    └── index.html              # Frontend HTML with CSS and JavaScript

Model Details
The application uses a LogisticRegression model trained on a credit card transaction dataset. It expects 30 numerical features: Time, Amount, and 28 anonymized features (V1 through V28) which are the result of a PCA transformation. The model outputs a binary prediction: 0 for a legitimate transaction and 1 for a fraudulent transaction.