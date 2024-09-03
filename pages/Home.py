import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Churn Prediction App',
    page_icon= ':machine:',
    layout='wide'
)

st.title("Data page")

#Load data

st.cache_data(persist=True)
def load_data():
    data = pd.read_csv('churn_prime.csv')
    return data

st.dataframe(load_data())
