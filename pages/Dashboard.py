import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sn
import matplotlib as pl

st.title('Customer Churn Dashboard')

# Load data
st.cache_data(persist=True)
def load_data():
    data = pd.read_csv('churn_prime.csv')
    return data

# Display data
data = load_data()
st.dataframe(data.head())


#EDA Dashboard

st.subheader("EDA Dashboard")
st.markdown (""" 
            - This dashboard provides an exploratory data analysis of the customer churn dataset.
            - The data includes ...
             """)

# 
col1, col2= st.columns(2)

with col1:



# KPIs Dashboard 
st.subheader("KPIs Dashboard")
st.markdown (""" 
            - This dashboard provides key performance indicators (KPIs) of the customer churn dataset.
            - The KPIs include ...
            - Below are Visuals for the KPIs each with detailed explanation of the visual interpretation
             """)



# Pie chart for churn distribution
fig = px.pie(data, values='Churn', names='Contract', title='Churn Distribution by Contract Type')
st.plotly_chart(fig)

# Bar chart for average charges by contract type
fig = px.bar(data, x='Contract', y='MonthlyCharges', title='Average Monthly Charges by Contract Type')
st.plotly_chart(fig)

# Box plot for tenure distribution by contract type
fig = px.box(data, x='Contract', y='tenure', title='Tenure Distribution by Contract Type')
st.plotly_chart(fig)

# Scatter plot for tenure and monthly charges
fig = px.scatter(data, x='tenure', y='MonthlyCharges', color='Churn', title='Tenure vs Monthly Charges')
st.plotly_chart(fig)

# Line chart for total charges over time
fig = go.Figure(go.Scatter(x=data['tenure'], y=data['TotalCharges'], mode='lines', name='Total Charges'))
st.plotly_chart(fig)

# Heatmap for correlation matrix
corr_matrix = data.corr()
fig = go.Figure(go.Heatmap(z=corr_matrix.values, x=corr_matrix.columns, y=corr_matrix.columns, colorscale='Bluered'))
st.plotly_chart(fig)