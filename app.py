from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained Logistic Regression model from the .pkl file
try:
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    print("Error: 'model.pkl' not found. Please ensure the model file is in the same directory.")
    exit()

# Define the feature names in the correct order as expected by the model
feature_names = [
    'Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
    'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount'
]

@app.route('/')
def home():
    """Renders the main page with the prediction form."""
    return render_template('index.html', prediction_text="")

@app.route('/predict', methods=['POST'])
def predict():
    """Handles the form submission and returns the prediction."""
    try:
        # Get the form data from the request
        form_data = request.form.to_dict()

        # Extract values in the correct order, converting them to float
        input_data = [float(form_data[name]) for name in feature_names]

        # Create a pandas DataFrame for prediction
        data_df = pd.DataFrame([input_data], columns=feature_names)

        # Make a prediction using the loaded model
        prediction = model.predict(data_df)[0]

        # Interpret the prediction result
        if prediction == 0:
            result = "Legitimate Transaction"
        else:
            result = "Fraudulent Transaction"

        # Render the page again with the prediction result
        return render_template('index.html', prediction_text=f'The transaction is: {result}')

    except Exception as e:
        # Handle any errors that occur during processing
        return render_template('index.html', prediction_text=f'An error occurred: {e}')

if __name__ == '__main__':
    app.run(debug=True)