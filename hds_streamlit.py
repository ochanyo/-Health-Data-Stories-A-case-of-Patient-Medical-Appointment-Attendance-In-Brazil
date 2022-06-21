import streamlit as st
import joblib
import pandas as pd

st.write("# Medical Appointment Attendance In Brazil")
#we have about 8 variables to collect from the user
#split the app into 2 columns to improve the UI
col1,col2=st.columns(2)
gender = col1.selectbox("Select your gender",["Male", "Female"])
age=col2.number_input("What is your Age?")
scholarship=col1.selectbox("Did you receive the Scholarship?",["Yes","No"])
hipertension=col2.selectbox("Do you suffer from hypertension?",["Yes","No"])
diabetes=col1.selectbox("Do you have diabetes?",["Yes","No"])
alcoholism=col2.selectbox("Do you drink alcohol?",["Yes","No"])
handcap=col1.selectbox("Do you have any phsyical impairment?",["Yes","No"])
sms_received=col2.selectbox("Did you recieve an SMS reminding you of your appointment?",["Yes","No"])

#st.button('Predict')
   
#writing code to transform user input
#user input is in string we need it in a form the model can read

df_pred = pd.DataFrame([[gender,age,scholarship,hipertension,diabetes,alcoholism,handcap,sms_received]],columns= ['gender','age','scholarship','hipertension','diabetes','alcoholism','handcap','sms_received'])

df_pred['gender'] = df_pred['gender'].apply(lambda x: 1 if x == "Male" else 0)
df_pred['scholarship'] = df_pred['scholarship'].apply(lambda x: 1 if x == "Yes" else 0)
df_pred['hipertension'] = df_pred['hipertension'].apply(lambda x: 1 if x == "Yes" else 0)
df_pred['diabetes'] = df_pred['diabetes'].apply(lambda x: 1 if x == "Yes" else 0)
df_pred['alcoholism'] = df_pred['alcoholism'].apply(lambda x: 1 if x == "Yes" else 0)
df_pred['handcap'] = df_pred['handcap'].apply(lambda x: 1 if x == "Yes" else 0)
df_pred['sms_received'] = df_pred['sms_received'].apply(lambda x: 1 if x == "Yes" else 0)



#loading the model
model=joblib.load('hds_rf_model.pkl')
prediction=model.predict(df_pred)

if st.button('Predict'):
    if(prediction[0]==0):
        st.write('<p class="big-font">You are likely to attend your medical appointment.</p>',unsafe_allow_html=True)
else:
        st.write('<p class="big-font">You are likely to miss your medical appointment  </p>',unsafe_allow_html=True)

