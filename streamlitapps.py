import streamlit as st 
import pandas as pd
import time
email = st.text_input("Enter Email")
password=st.text_input("Enter Password", type="password")
gender=st.selectbox("Select Gender",["male","Female","Others"])
btn= st.button("Login")

if btn:
    if email =="123@gmail.com" and password=="1234":
        st.balloons()
        time.sleep(1)
        st.snow()
    else:
        st.error("Login Failed")
        
        
        
file = st.file_uploader("Uplord a csv file")

if file is not None:
    df= pd.read_csv(file)
    st.dataframe(df.describe())
    