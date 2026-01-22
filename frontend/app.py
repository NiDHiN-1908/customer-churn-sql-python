import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

st.title("Customer Churn Prediction Dashboard")

df = pd.read_csv("python/churn_predictions.csv")

st.metric("Total Customers", len(df))
st.metric("Churned Customers", int(df["predicted_churn"].sum()))

st.dataframe(df)

st.success("Predictions loaded successfully.")
