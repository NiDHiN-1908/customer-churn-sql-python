# ChurnIQ – Data-Driven Customer Retention System
## Overview

ChurnIQ is an end-to-end customer churn prediction platform built using PostgreSQL, Python, and Machine Learning.
It analyzes real-world telecom customer data and predicts which users are likely to churn, enabling businesses to take proactive retention actions.

### Workflow:
Database → Feature Engineering → Machine Learning → Business Dashboard

---------------------------------------------------------------------------------
## Business Use Case

Customer churn directly reduces revenue and increases acquisition costs.
ChurnIQ helps organizations:

* Identify customers with a high risk of churn

* Take proactive retention actions

* Improve retention strategies

* Make data-driven business decisions

---------------------------------------------------------------------------------

## Technology Stack

| Layer            | Tools                              |
| ---------------- | ---------------------------------- |
| Database         | PostgreSQL                         |
| Data Processing  | Python, Pandas                     |
| Machine Learning | Scikit-learn (Logistic Regression) |
| Visualization    | Streamlit, Plotly                  |
| Connectivity     | psycopg2                           |
| Model Storage    | joblib                             |

--------------------------------------------------------------------------------

## Machine Learning Details

| Item            | Description                                             |
| --------------- | ------------------------------------------------------- |
| Problem Type    | Binary Classification                                   |
| Target Variable | churn (0 = retained, 1 = churned)                       |
| Features        | tenure, age, income, longmon, tollmon, wiremon, cardmon |
| Model           | Logistic Regression + StandardScaler                    |
| Metrics         | Accuracy, Precision, Recall, F1-Score, ROC-AUC          |

--------------------------------------------------------------------------------

## Project Structure

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
│   ├── predict.py
│   └── archive/
│       ├── analysis_legacy.py
│       ├── preprocess.py
│       └── extract_features.py
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

-----------------------------------------------------------------------------

## System Workflow

1. Load customer data into PostgreSQL

2. Create SQL views for ML features

3. Train Logistic Regression model

4. Generate churn predictions

5. Visualize insights in Streamlit dashboard

-----------------------------------------------------------------------------

## Installation & Execution
### 1. Install dependencies
pip install -r requirements.txt

### 2. Setup database (psql)
\i database/schema.sql
\i database/views.sql

### 3. Import dataset
\copy telco_customers FROM 'data/telco_churn_kaggle.csv' CSV HEADER;

### 4. Train model
python ml/train_model.py

### 5. Generate predictions
python python/predict.py

### 6. Run dashboard
streamlit run frontend/app.py

-----------------------------------------------------------------------------

## Dashboard Output

The dashboard provides:

* Total customers

* Predicted churn count

* Churn probability distribution

* High-risk customer list

* Model performance (ROC curve & confusion matrix)

---------------------------------------------------------------------------------

## Business Impact

* Enables early identification of churn-prone customers

* Supports targeted retention strategies

* Reduces revenue loss

* Converts raw data into business actions

--------------------------------------------------------------------------------

## Limitations

* Small dataset (200 records)

* Low recall for churn class

* No time-series behavior modeling

--------------------------------------------------------------------------------

## Future Scope

* Class imbalance handling

* Advanced models (Random Forest, XGBoost)

* Real-time churn monitoring

* Cloud deployment

-------------------------------------------------------------------------------

## Author

### Nidhin
Aspiring Data Scientist | Machine Learning Enthusiast