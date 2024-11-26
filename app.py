import streamlit as st 
import pandas as pd 
import pickle as pk 
  
lr_model = pk.load(open("lr.pkl","rb"))
scaller = pk.load(open("scaller.pkl","rb"))

st.header("Loan prediction app")

nod= st.slider("No of Dependents",0,5)
education= st.selectbox("Education",["Graduate","Non_Graguate"])
self_emp= st.selectbox("Self_Employed",["yes","No"])
ann_income= st.slider("Annum_Income",0,5000000)
loan_amt= st.slider("Loan_amount",0,5000000)
loan_term= st.slider("Loan_term",0,24)
cibil_scr= st.slider("Cibil_Score",0,1000)
total_asset= st.slider("Total_asset",0,50000000)



if st.button("predict"):
    

    if education == "Graduate":
        education=1
    else:
        education=0
    
    if self_emp == "yes":
        self_emp=1
    else:
        self_emp=0

    
    pred_data = pd.DataFrame([[nod,education,self_emp,ann_income,loan_amt,loan_term,cibil_scr,total_asset]],columns=['no_of_dependents','education','self_employed','income_annum','loan_amount','loan_term','cibil_score','Total_asset'])

    print(pred_data)
    pred_data = scaller.transform(pred_data)
    pred= lr_model.predict(pred_data)

    if pred[0]==1:
        st.markdown("Loan is Approved")
    else:   
        st.markdown("Loan is Not_Approved")

   