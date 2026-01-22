import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
df = pd.read_csv("data/telco_churn_kaggle.csv")

# Clean TotalCharges column
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.dropna(inplace=True)

# Encode categorical columns
for col in df.select_dtypes(include="object"):
    df[col] = LabelEncoder().fit_transform(df[col])

# Features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save model
joblib.dump(model, "ml/churn_model.pkl")

print("Model trained and saved successfully.")
