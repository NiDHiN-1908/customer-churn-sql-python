# ChurnIQ – Data-Driven Customer Retention System
## Overview

ChurnIQ is an end-to-end customer churn prediction platform built using PostgreSQL, Python, and Machine Learning.
It analyzes real-world telecom customer data and predicts which users are likely to churn, enabling businesses to take proactive retention actions.

Workflow: Database → Feature Engineering → Machine Learning → Business Dashboard

Business Use Case

Customer churn directly reduces revenue and increases acquisition costs.
ChurnIQ helps organizations:

Identify customers with a high risk of churn

Take proactive retention actions

Improve retention strategies

Make data-driven business decisions

## Technology Stack

| Layer            | Tools                              |
| ---------------- | ---------------------------------- |
| Database         | PostgreSQL                         |
| Data Processing  | Python, Pandas                     |
| Machine Learning | Scikit-learn (Logistic Regression) |
| Visualization    | Streamlit, Plotly                  |
| Connectivity     | psycopg2                           |
| Model Storage    | joblib                             |

## Machine Learning Details

| Item            | Description                                             |
| --------------- | ------------------------------------------------------- |
| Problem Type    | Binary Classification                                   |
| Target Variable | churn (0 = retained, 1 = churned)                       |
| Features        | tenure, age, income, longmon, tollmon, wiremon, cardmon |
| Model           | Logistic Regression + StandardScaler                    |
| Metrics         | Accuracy, Precision, Recall, F1-Score                   |

## Project Structure

churn_analysis_project/
│
├── data/                         # Raw dataset
│   └── telco_churn_kaggle.csv
│
├── database/                     # PostgreSQL schema & views
│   ├── schema.sql
│   └── views.sql
│
├── ml/                           # Model training artifacts
│   ├── train_model.py
│   └── churn_model.pkl
│
├── python/                       # Prediction & utilities
│   ├── predict.py
│   └── archive/                  # Legacy experimental scripts
│       ├── analysis_legacy.py
│       ├── preprocess.py
│       └── extract_features.py
│
├── frontend/                     # Dashboard
│   └── app.py
│
├── report/                       # Documentation & evidence
│   └── screenshots/
│
├── .env.example                  # Environment variables
├── .gitignore
├── requirements.txt
└── README.md


## System Workflow

Load customer data into PostgreSQL

Create SQL view for ML features

Train Logistic Regression model using Python

Generate churn predictions

Visualize results in Streamlit dashboard

## Installation & Execution

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

## Dashboard Output

The dashboard provides:

Total customers

Predicted churn count

Churn probability distribution

High-risk customer list

## Future Scope

Advanced models (Random Forest, XGBoost)

Model evaluation dashboard

Real-time churn monitoring

Cloud deployment

## Author

Nidhin
Aspiring Data Scientist | Machine Learning Enthusiast
