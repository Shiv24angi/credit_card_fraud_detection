# Credit Card Fraud Detection
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/Shiv24angi/credit_card_fraud_detection)

This project is a web application that uses a machine learning model to detect credit card fraud in real-time. It features a simple user interface built with Flask and HTML, allowing users to input transaction data and receive an instant prediction on whether the transaction is legitimate or fraudulent.

## Features
- **Interactive Web Dashboard**: A clean and responsive web form built with HTML and CSS for data input.
- **Real-time Predictions**: Leverages a pre-trained Logistic Regression model to classify transactions instantly.
- **Flask Backend**: A lightweight Flask server handles prediction requests and serves the web interface.
- **Clear Visual Feedback**: The prediction result is displayed with distinct colors for easy interpretation (green for legitimate, red for fraudulent).
- **Standalone Model Training**: Includes the Jupyter Notebook (`Project_10_Credit_Card_Fraud_Detection.ipynb`) detailing the entire process from data exploration and preprocessing to model training and evaluation.

## Model Details
The prediction model is a **Logistic Regression** classifier trained on the Kaggle "Credit Card Fraud Detection" dataset.

- **Dataset**: The dataset contains transactions made by European cardholders. To protect confidentiality, the original features have been transformed via Principal Component Analysis (PCA), resulting in 28 numerical features (`V1` to `V28`), in addition to `Time` and `Amount`.
- **Data Preprocessing**: The original dataset is highly imbalanced, with fraudulent transactions accounting for a very small percentage of the total. To address this, **under-sampling** was performed to create a balanced dataset for training, ensuring the model learns effectively from both fraudulent and legitimate transaction patterns.
- **Performance**: After training on the balanced dataset, the model achieves an accuracy of approximately **93.4%** on the test set.

## Project Structure
```
.
├── Project_10_Credit_Card_Fraud_Detection.ipynb # Jupyter Notebook for data analysis and model training
├── app.py                      # Flask application for the web interface
├── model.pkl                   # The pre-trained Logistic Regression model
└── templates/
    └── index.html              # Frontend HTML page for the dashboard
```

## Technology Stack
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Frontend**: HTML, CSS

## Setup and Usage
To run this project locally, follow these steps:

### Prerequisites
- Python 3.x
- `pip` (Python package installer)

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/shiv24angi/credit_card_fraud_detection.git
    cd credit_card_fraud_detection
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install Flask pandas scikit-learn numpy
    ```

3.  **Run the Flask application:**
    ```bash
    python app.py
    ```

### Using the Application
1.  Once the server is running, open your web browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```
2.  You will see the "Credit Card Fraud Detection Dashboard".
3.  Fill in all 30 input fields (`Time`, `Amount`, and `V1` through `V28`) with transaction data.
4.  Click the **"Predict Fraud"** button.
5.  The prediction result will be displayed on the same page below the form.