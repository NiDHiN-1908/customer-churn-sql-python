import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("data/telco_churn_kaggle.csv")
df.columns = df.columns.str.strip()

# Create SQL-like features
train_df = pd.DataFrame()
train_df["age"] = df["age"]
train_df["total_logins"] = df["longten"]
train_df["avg_session"] = df["longmon"]
train_df["total_payments"] = df["cardten"]
train_df["failed_payments"] = df["tollten"]
train_df["churn"] = df["churn"]

X = train_df.drop("churn", axis=1)
y = train_df["churn"]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

joblib.dump(model, "ml/churn_model.pkl")
print("Aligned model trained.")
