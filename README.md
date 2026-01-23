ChurnIQ – Data-Driven Customer Retention System
Overview

ChurnIQ is an end-to-end customer churn prediction platform built using PostgreSQL, Python, and Machine Learning.
It analyzes real-world telecom customer data and predicts which users are likely to churn, enabling businesses to take proactive retention actions.

This project demonstrates a complete data science workflow:

Database → Feature Engineering → Machine Learning → Business Dashboard

Business Use Case

Customer churn directly reduces revenue and increases acquisition costs.
ChurnIQ helps organizations:

Identify customers with a high risk of churn

Take proactive retention actions

Improve customer retention strategies

Make data-driven business decisions

Technology Stack

Database: PostgreSQL

Data Processing: Python, Pandas

Machine Learning: Scikit-learn (Logistic Regression)

Visualization: Streamlit

Connectivity: psycopg2

Model Storage: joblib

Machine Learning Details

Problem Type: Binary Classification

Target Variable: churn (0 = retained, 1 = churned)

Features: tenure, age, income, longmon, tollmon, wiremon, cardmon

Model: Logistic Regression with StandardScaler

Evaluation Metrics: Accuracy, Precision, Recall, F1-Score

Project Structure

churn_analysis_project/
│
├── data/
│   └── telco_churn_kaggle.csv
│
├── database/
│   ├── schema.sql
│   └── views.sql
│
├── ml/
│   ├── train_model.py
│   └── churn_model.pkl
│
├── python/
│   └── predict.py
│
├── frontend/
│   └── app.py
│
├── report/
│   └── screenshots/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

System Workflow

Load customer data into PostgreSQL

Create SQL view for ML features

Train Logistic Regression model using Python

Generate churn predictions

Display insights in Streamlit dashboard

Installation & Execution
1. Install Dependencies
pip install -r requirements.txt

2. Setup Database
\i database/schema.sql
\i database/views.sql

3. Import Dataset
\copy telco_customers FROM 'data/telco_churn_kaggle.csv' CSV HEADER;

4. Train Model
python ml/train_model.py

5. Generate Predictions
python python/predict.py

6. Run Dashboard
streamlit run frontend/app.py

Dashboard Output

The Streamlit application displays:

Total customers

Predicted churn count

Churn probability per customer

High-risk customer list

Future Scope

Integration with live customer data

Advanced ML models (Random Forest, XGBoost)

Model performance dashboard

Cloud deployment

Author

Nidhin
Aspiring Data Scientist | Machine Learning Enthusiast