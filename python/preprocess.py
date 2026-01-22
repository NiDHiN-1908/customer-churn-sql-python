import pandas as pd

df = pd.read_csv("python/sql_features.csv")

# Drop categorical columns not in model
df = df.drop(columns=["region", "plan_type"])

df.to_csv("python/sql_features_encoded.csv", index=False)
print("Preprocessing completed.")
