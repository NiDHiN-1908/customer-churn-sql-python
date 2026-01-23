import psycopg2
import pandas as pd
import joblib

# Load trained model
model = joblib.load("ml/churn_model.pkl")

# Connect to database
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="1908",
    database="churn_analysis"
)

# Load same features used in training
df = pd.read_sql("SELECT * FROM churn_features", conn)

X = df.drop("churn", axis=1)

# Predict churn label and probability
df["predicted_churn"] = model.predict(X)
df["churn_probability"] = model.predict_proba(X)[:, 1]

# Save predictions
df.to_csv("python/churn_predictions.csv", index=False)
print("Predictions generated from PostgreSQL.")
