import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

st.title("Customer Churn Prediction Dashboard")

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1908",
    database="churn_analysis"
)

query = """
SELECT
    c.customer_id,
    c.age,
    c.region,
    s.plan_type,

    COUNT(u.usage_id) AS total_logins,
    AVG(u.session_minutes) AS avg_session_minutes,
    SUM(CASE WHEN p.payment_status = 'failed' THEN 1 ELSE 0 END) AS failed_payments,

    CASE
        WHEN s.status = 'cancelled'
             OR MAX(u.login_date) < '2023-10-31' - INTERVAL 30 DAY
        THEN 1
        ELSE 0
    END AS churn_flag

FROM customers c
JOIN subscriptions s ON c.customer_id = s.customer_id
LEFT JOIN usage_logs u ON c.customer_id = u.customer_id
LEFT JOIN payments p ON c.customer_id = p.customer_id

GROUP BY
    c.customer_id,
    c.age,
    c.region,
    s.plan_type,
    s.status;
"""

df = pd.read_sql(query, conn)
df.fillna(0, inplace=True)

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", len(df))
col2.metric("Churned Customers", int(df["churn_flag"].sum()))
col3.metric("Retention Rate", f"{(1 - df['churn_flag'].mean()) * 100:.1f}%")

st.divider()

st.subheader("Churn Distribution")
st.bar_chart(df["churn_flag"].value_counts())

st.subheader("High-Risk Customers")
st.dataframe(df[df["churn_flag"] == 1])
