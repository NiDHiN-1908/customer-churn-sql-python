import psycopg2
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay

model = joblib.load("ml/churn_model.pkl")

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="1908",
    database="churn_analysis"
)

df = pd.read_sql("SELECT * FROM churn_features", conn)
X = df.drop("churn", axis=1)
y = df["churn"]

# Confusion Matrix
ConfusionMatrixDisplay.from_estimator(model, X, y)
plt.title("Confusion Matrix")
plt.savefig("report/screenshots/confusion_matrix.png")

# ROC Curve
RocCurveDisplay.from_estimator(model, X, y)
plt.title("ROC Curve")
plt.savefig("report/screenshots/roc_curve.png")
