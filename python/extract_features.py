import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="1908",
    database="churn_analysis"
)

query = "SELECT * FROM churn_features;"
df = pd.read_sql(query, conn)

df.to_csv("python/sql_features.csv", index=False)
print("Features extracted from PostgreSQL.")
