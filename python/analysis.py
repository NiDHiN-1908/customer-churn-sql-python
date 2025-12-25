import mysql.connector
import pandas as pd

print("Starting Churn Analysis Project")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1908",
    database="churn_analysis"
)

print("Database connection successful")

# Pull SQL feature dataset into Python

query = """
SELECT
    c.customer_id,
    c.age,
    c.region,
    s.plan_type,

    COUNT(u.usage_id) AS total_logins,
    AVG(u.session_minutes) AS avg_session_minutes,
    DATEDIFF(CURDATE(), MAX(u.login_date)) AS days_since_last_login,

    COUNT(p.payment_id) AS total_payments,
    SUM(CASE WHEN p.payment_status = 'failed' THEN 1 ELSE 0 END) AS failed_payments,

    CASE
        WHEN s.status = 'cancelled'
             OR MAX(u.login_date) < '2023-10-31' - INTERVAL 30 DAY
        THEN 1
        ELSE 0
    END AS churn_flag

FROM customers c
JOIN subscriptions s
    ON c.customer_id = s.customer_id
LEFT JOIN usage_logs u
    ON c.customer_id = u.customer_id
LEFT JOIN payments p
    ON c.customer_id = p.customer_id

GROUP BY
    c.customer_id,
    c.age,
    c.region,
    s.plan_type,
    s.status;
"""

df = pd.read_sql(query, conn)

print(df)



print("\nDataset shape:", df.shape)
print("\nChurn distribution:")
print(df["churn_flag"].value_counts())


# PREPARE DATA FOR MODELING

# Handle missing values
df.fillna(0, inplace=True)

# Encode categorical variables
df_encoded = pd.get_dummies(
    df,
    columns=["region", "plan_type"],
    drop_first=True
)

print("\nEncoded dataset:")
print(df_encoded)


# BUILD THE CHURN PREDICTION MODEL

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

X = df_encoded.drop(columns=["customer_id", "churn_flag"])
y = df_encoded["churn_flag"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nModel Evaluation:")
print(classification_report(y_test, y_pred))

