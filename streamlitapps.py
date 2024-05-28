import streamlit as st 
import time
email = st.text_input("Enter Email")
password=st.text_input("Enter Password", type="password")
btn= st.button("Login")

if btn:
    if email =="123@gmail.com" and password=="1234":
        st.balloons()
        time.sleep(1)
        st.snow()
    else:
        st.error("Login Failed")