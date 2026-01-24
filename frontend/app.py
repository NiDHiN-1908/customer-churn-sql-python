import streamlit as st
import pandas as pd
import psycopg2
import joblib
import plotly.express as px

st.set_page_config(page_title="ChurnIQ Dashboard", layout="wide")

# ----------------------------
# Database Connection
# ----------------------------
@st.cache_data
def load_data():
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="1908",
        database="churn_analysis"
    )
    return pd.read_sql("SELECT * FROM churn_features", conn)

df = load_data()

# ----------------------------
# Load Model
# ----------------------------
model = joblib.load("ml/churn_model.pkl")

X = df.drop("churn", axis=1)
df["churn_probability"] = model.predict_proba(X)[:, 1]
df["predicted_churn"] = model.predict(X)

# ----------------------------
# Header
# ----------------------------
st.title("ChurnIQ – Customer Churn Intelligence Dashboard")
st.caption("SQL + Python + Machine Learning")

# ----------------------------
# KPIs
# ----------------------------
total_customers = len(df)
churned = int(df["predicted_churn"].sum())
retention = round((1 - churned / total_customers) * 100, 2)

c1, c2, c3 = st.columns(3)
c1.metric("Total Customers", total_customers)
c2.metric("Predicted Churn", churned)
c3.metric("Retention Rate (%)", retention)

st.divider()

# ----------------------------
# Visualizations
# ----------------------------
st.subheader("Churn Distribution")
fig1 = px.pie(df, names="predicted_churn", title="Predicted Churn Split")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Churn Probability Distribution")
fig2 = px.histogram(df, x="churn_probability", nbins=20)
st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ----------------------------
# High-Risk Tables
# ----------------------------
st.subheader("High-Risk Customers")

top_n = st.slider("Select number of customers to display", 10, len(df), 20)

st.dataframe(
    df.sort_values("churn_probability", ascending=False).head(top_n),
    use_container_width=True
)

st.subheader("All Predicted Churn Customers")

churn_only = df[df["predicted_churn"] == 1]
st.write(f"Total churn-predicted customers: {len(churn_only)}")

st.dataframe(
    churn_only.sort_values("churn_probability", ascending=False),
    use_container_width=True
)

st.divider()

# ----------------------------
# Model Evaluation
# ----------------------------
st.subheader("Model Performance")

col1, col2 = st.columns(2)
col1.image("report/screenshots/confusion_matrix.png", caption="Confusion Matrix")
col2.image("report/screenshots/roc_curve.png", caption="ROC Curve")
