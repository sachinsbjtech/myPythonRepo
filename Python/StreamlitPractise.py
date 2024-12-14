import streamlit as st
import pandas as pd

st.write("""
# My First StramLit App
Hello *Sachin!*
""")

df = pd.read_csv("Salary_Data-1.csv")

st.line_chart(df)
st.bar_chart(df)

st.date_input("Select date of Joining")
file = st.file_uploader("Upload Input File")
print(type(file))