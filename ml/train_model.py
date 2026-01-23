import psycopg2
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="1908",
    database="churn_analysis"
)

# Load features directly from SQL view
df = pd.read_sql("SELECT * FROM churn_features", conn)

# Split features and target
X = df.drop("churn", axis=1)
y = df["churn"]

# ML pipeline: scaling + logistic regression
pipeline = Pipeline([
    ("scaler", StandardScaler()),     # Normalize numeric features
    ("model", LogisticRegression(max_iter=1000))
])

# Train model
pipeline.fit(X, y)

# Save trained model
joblib.dump(pipeline, "ml/churn_model.pkl")
print("Model trained from PostgreSQL and saved.")
