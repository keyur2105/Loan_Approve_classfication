import streamlit as st
import pandas as pd
import pickle as pk

# Load model and scaler
lr_model = pk.load(open("lr.pkl", "rb"))
scaller = pk.load(open("scaller.pkl", "rb"))

st.markdown("""
    <style>
    /* Light theme styling for the Loan Prediction App */
    body {
        background-color: #f9f9f9;
        font-family: Arial, sans-serif;
        color: #333;
    }

    /* Card style for input container */
    .input-card {
        display:none;
    }

    /* Styling sliders */
    .st-an {
        color: #007bff !important;
        background-color: #f9f9f9 !important;
        border-radius: 10px !important;
    }

    /* Dropdowns and select boxes */
    .st-b1 {
        border: 1px solid #ccc !important;
        box-shadow: none !important;
        background-color: #fff !important;
        color: #333 !important;
        border-radius: 5px;
    }
    
    .st-bw{
        display:none;
    }

    .st-b1:hover {
        border: 1px solid #007bff !important;
    }

    /* Buttons */
    .st-b1>button {
        background-color: #007bff !important;
        border: none !important;
        color: white !important;
        border-radius: 5px !important;
        padding: 10px 20px !important;
        font-size: 14px !important;
        cursor: pointer !important;
    }

    .st-b1>button:hover {
        background-color: #0056b3 !important;
    }
    
    # button{
    #     border:none;
    #     background:none;
    #         }

    /* Results styling */
    .result-text {
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit app header
st.header("🌟 Loan Prediction App 🌟")

# Card-style container for inputs
with st.container():
    st.markdown("<div class='input-card'>", unsafe_allow_html=True)
    
    # Input elements
    nod = st.slider("Number of Dependents", 0, 5)
    education = st.selectbox("Education Level", ["Graduate", "Non_Graduate"])
    self_emp = st.selectbox("Self-Employed", ["Yes", "No"])
    ann_income = st.slider("Annual Income (INR)", 0, 5000000)
    loan_amt = st.slider("Loan Amount (INR)", 0, 5000000)
    loan_term = st.slider("Loan Term (Years)", 0, 24)
    cibil_scr = st.slider("CIBIL Score", 0, 1000)
    total_asset = st.slider("Total Assets (INR)", 0, 50000000)

    st.markdown("</div>", unsafe_allow_html=True)

# Prediction button and logic
if st.button("Predict"):
    # Data preprocessing based on input
    if education == "Graduate":
        education = 1
    else:
        education = 0

    if self_emp == "Yes":
        self_emp = 1
    else:
        self_emp = 0

    # Creating DataFrame for prediction
    pred_data = pd.DataFrame([[nod, education, self_emp, ann_income, loan_amt, loan_term, cibil_scr, total_asset]],
                             columns=['no_of_dependents', 'education', 'self_employed', 'income_annum', 'loan_amount', 'loan_term', 'cibil_score', 'Total_asset'])

    # Scaling and prediction
    pred_data = scaller.transform(pred_data)
    pred = lr_model.predict(pred_data)

    # Display prediction result
    if pred[0] == 1:
        st.markdown("<div class='result-text' style='color: green;'>Loan Approved..! ✅</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='result-text' style='color: red;'>Loan Not Approved..! ❌</div>", unsafe_allow_html=True)
