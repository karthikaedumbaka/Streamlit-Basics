import streamlit as st
import pandas as pd

st.title('This is Title command')
st.header("This is header command")
st.subheader("This is subheader command")


st.write("the is write command")

st.markdown("""
            - 1st markdown
            - 2nd markdown
            - 3rd markdown
            
            """)


st.code("""
def python(input):
    return "this is code fucntion"
 
"""
)


st.latex("x^2 +y^2 = 10")

df= pd.DataFrame({
    "name ":["karthik","balaji","klay"],
    "marks ":["99","85","100"],
    "package ": ["70000","60000","90000"] 
})

st.dataframe(df)


st.metric("Revenue","Rs 3L","+3%")

st.json({
    "name ":["karthik","balaji","klay"],
    "marks ":["99","85","100"],
    "package ": ["70000","60000","90000"] 
})

st.image("image.png")


st.sidebar.title("This is side Bar")



st.write("to create a muli columns")
col1,col2,col3=st.columns(3)

with col1:
    st.image("image.png")
with col2:
    st.image("image.png")
with col3:
    st.image("image.png")

st.write("to create a messages")
st.error("login failed")
st.success("login done")
st.info("this is info")
st.warning("this is login successfull")



import time
bar=st.progress(0)

for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)
st.write("done")