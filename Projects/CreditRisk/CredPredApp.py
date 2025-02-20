import pickle 
import streamlit as st 
from PIL import Image 
import numpy as np
import pandas as pd

## load the saved model
pickle_in = open(r'C:\Users\shachini dinushika\Documents\100daysPy\45daysDS&ML\Rf_clf.pkl', 'rb') 
Rf_clf = pickle.load(pickle_in)

st.sidebar.header('User input credit risk features')

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

historical_data = pd.read_csv(r'C:\Users\shachini dinushika\Documents\Data\CreditRisk\credit_risk_dataset_cleaned.csv')

# historical_data['default_rate'] = historical_data['loan_status'].sum()/len(historical_data)

def plot_income_distribution(user_income):
    plt.figure(figsize=(6,4))

    sns.histplot(historical_data['person_income'], bins=30, kde=True, color='blue', alpha=0.5, label='Historical Data')
    plt.axvline(user_income, color='red', linestyle='dashed', linewidth=2, label='User Income')
    
    plt.xlabel('Income')
    plt.ylabel('Frequency')
    plt.title('Income Distribution')
    plt.legend()
    
    st.pyplot(plt)

def plot_loan_vs_interest(user_loan, user_interest):
    plt.figure(figsize=(6,4))

    sns.scatterplot(x=historical_data['loan_amnt'],y=historical_data['loan_int_rate'], alpha=0.5, label='Historical Data')
    
    plt.scatter(user_loan, user_interest, color='red', s=100, label='User Input')
    plt.xlabel('Loan amount')
    plt.ylabel('Interest rate')
    plt.title('Loan amount vs Interest rate')
    plt.legend()

    st.pyplot(plt)

def plot_confidence(prob_default):
    fig = go.Figure(go.Indicator(
        mode='gauge+number',
        value=prob_default * 100,
        title={'text': 'Risk Confidence'},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': 'red' if prob_default > 0.5 else 'green'}}))

    st.plotly_chart(fig)
    

def input_data():

    person_income = st.sidebar.number_input('Enter person income', key='person_income')
    loan_int_rate = st.sidebar.slider('Select interest rate', min_value=0, max_value=100, value=10, key='int_rate')
    person_age = st.sidebar.slider('Select person age', min_value=0, max_value=100, value=20, key='age')
    loan_amnt = st.sidebar.number_input('Enter loan amount', key='loan_amnt')
    loan_percent_income = st.sidebar.number_input('Enter loan percent income', key='loan_percent')
    person_emp_length = st.sidebar.number_input('Enter employment duration', key='emp_length')
    cb_person_cred_hist_length = st.sidebar.number_input('Enter credit history duration', key='cred_hist')

    try:
        person_income = float(person_income) if person_income else 0.0
        loan_amnt     = float(loan_amnt) if loan_amnt else 0.0
        loan_percent_income = float(loan_percent_income) if loan_percent_income else 0.0
        person_emp_length = int(person_emp_length) if person_emp_length else 0.0
        cb_person_cred_hist_length = int(cb_person_cred_hist_length) if cb_person_cred_hist_length else 0.0
    
    except:
        st.sidebar.error('⚠️ Please enter valid data')


    data = pd.DataFrame([[person_income,loan_int_rate,person_age,loan_amnt,
                          loan_percent_income,person_emp_length,cb_person_cred_hist_length]],
                        columns = ['person_income','loan_int_rate','person_age',
                                   'loan_amnt','loan_percent_income',
                                   'person_emp_length','cb_person_cred_hist_length'] )
    

    return  data

def prediction(data):
    prediction = Rf_clf.predict(data)
    return prediction

def prediction_proba(data):
   prediction_probability = Rf_clf.predict_proba(data)
   return prediction_probability


def main():

    st.markdown('# 🏦 Prediction of credit risk')

    col1, col2 = st.columns(2)

    result = None

    user_data = input_data()

    with col1: 
        if user_data is not None:
          st.markdown(f"""### 🔍 User Input Summary""")
          st.dataframe(user_data.T) 
          
    
    with col2:
        if st.sidebar.button('Predict'): 
            try:
                result = prediction(user_data)
                pred_prob = prediction_proba(user_data)
            
                risk_status = 'Default' if result == 1 else  'Non-Default'

                st.subheader('Prediction:')

                st.success('The Customer is a {}'.format(risk_status)) 

                # #Confidence Gauge Chart
                # prob_default = prediction_proba(user_data)[0][1]
                # plot_confidence(prob_default)

                st.subheader('Prediction probability:')

                st.write(pred_prob)

            except ValueError as e:
                st.error(f'Error processing inputs: {e}')
        else:
            st.warning('❌ Please fill the fields with valid data')

    with st.expander(f"""### 📊 View Data Insights"""):
        col3, col4 = st.columns(2)

        with col3:
            plot_income_distribution(user_data['person_income'][0])

        with col4: 
            plot_loan_vs_interest(user_data['loan_amnt'][0], user_data['loan_int_rate'][0])

     
if __name__=='__main__': 
    main() 

