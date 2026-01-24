import psycopg2
import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# Load model
model = joblib.load("ml/churn_model.pkl")

# Load data from PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="1908",
    database="churn_analysis"
)

df = pd.read_sql("SELECT * FROM churn_features", conn)

X = df.drop("churn", axis=1)
y = df["churn"]

y_pred = model.predict(X)
y_prob = model.predict_proba(X)[:, 1]

print("Classification Report:")
print(classification_report(y, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y, y_pred))

print("ROC-AUC:", roc_auc_score(y, y_prob))
