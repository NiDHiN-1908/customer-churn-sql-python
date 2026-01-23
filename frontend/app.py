import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="ChurnIQ Dashboard", layout="wide")

st.title("ChurnIQ – Customer Retention Dashboard")

df = pd.read_csv("python/churn_predictions.csv")

total = len(df)
churned = (df["predicted_churn"] == 1).sum()
retained = total - churned

col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", total)
col2.metric("Predicted Churn", churned)
col3.metric("Retention", retained)

st.divider()

# Churn Distribution
st.subheader("Churn Distribution")
fig1 = px.pie(
    names=["Retained", "Churned"],
    values=[retained, churned],
    title="Customer Churn Split"
)
st.plotly_chart(fig1, use_container_width=True)

# Probability Distribution
st.subheader("Churn Risk Distribution")
fig2 = px.histogram(
    df,
    x="churn_probability",
    nbins=20,
    title="Churn Probability Distribution"
)
st.plotly_chart(fig2, use_container_width=True)

# High Risk Customers
st.subheader("Top 20 High-Risk Customers")
st.dataframe(df.sort_values("churn_probability", ascending=False).head(20))

st.success("Live churn analytics loaded.")
