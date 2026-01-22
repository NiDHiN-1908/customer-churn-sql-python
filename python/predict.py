import pandas as pd
import joblib

model = joblib.load("ml/churn_model.pkl")
df = pd.read_csv("python/sql_features_encoded.csv")

X = df.drop("customer_id", axis=1)
df["predicted_churn"] = model.predict(X)

df.to_csv("python/churn_predictions.csv", index=False)
print("Predictions generated.")
