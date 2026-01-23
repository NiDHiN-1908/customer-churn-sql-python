import streamlit as st
import pandas as pd

# Page layout
st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

st.title("Customer Churn Prediction Dashboard")

# Load predictions
df = pd.read_csv("python/churn_predictions.csv")

# KPI Metrics
total = len(df)
churned = (df["predicted_churn"] == 1).sum()

st.metric("Total Customers", total)
st.metric("Predicted Churn", churned)

# Show highest risk users
st.subheader("High Risk Customers")
st.dataframe(df.sort_values("churn_probability", ascending=False).head(20))

st.success("Predictions loaded successfully.")
