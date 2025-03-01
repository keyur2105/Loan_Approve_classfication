# Loan Prediction Application

## Overview
This Streamlit application predicts the approval status of a loan based on user inputs such as number of dependents, education level, employment status, annual income, loan amount, loan term, CIBIL score, and total assets.

## Features
Interactive sliders and selection boxes for user input.
Predictive analysis using a pre-trained logistic regression model.
Real-time display of loan approval status.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/keyur2105/Loan_Approve_classification.git

## File Structure

loan_prediction_app/
- │
- ├── app.py                   # Main Streamlit application
- ├── lr.pkl                   # Pre-trained logistic regression model
- ├── scaller.pkl              # Scaler for preprocessing input data
- └── requirements.txt         # List of Python dependencies

## Dependencies
- streamlit
- pandas
- scikit-learn

## Notes
- Ensure that lr.pkl and scaller.pkl are present in the same directory as app.py.
- Customize the input parameters and ranges in app.py as needed to fit your specific use case.
  
