# Customer Churn Prediction Using SQL and Python

This project implements an end-to-end customer churn prediction system designed to support business decision-making. It integrates a relational database with Python analytics, basic machine learning, and an interactive Streamlit dashboard to identify customers at risk of churn.

The focus of this project is on business relevance, data pipeline clarity, and explainability rather than complex modeling.


## Problem Statement

Customer churn leads to revenue loss and reduced growth.  
The objective of this project is to analyze customer behavior and predict churn using historical data, enabling businesses to take proactive retention actions.


## Tech Stack

- Database: MySQL  
- Programming Language: Python  
- Libraries: Pandas, NumPy, Scikit-learn, mysql-connector-python  
- Visualization and UI: Streamlit  
- Version Control: Git and GitHub  


## Project Structure

```text
churn_analysis_project/
├── database/
│   └── schema.sql
├── python/
│   └── analysis.py
├── frontend/
│   └── app.py
└── report/
```

- database contains the SQL schema  
- python contains data analysis and churn prediction logic  
- frontend contains the Streamlit dashboard  
- report is reserved for documentation and screenshots  



## Methodology

1. Designed a relational database with tables for customers, subscriptions, usage logs, and payments  
2. Inserted sample data to simulate real-world customer behavior  
3. Engineered churn-related features using SQL joins and aggregations  
4. Connected MySQL to Python using mysql-connector  
5. Cleaned and preprocessed data using Pandas  
6. Built a Logistic Regression model to predict customer churn  
7. Visualized churn metrics and high-risk customers using Streamlit  


## Key Features

- SQL-based feature engineering  
- Python–MySQL integration  
- Churn prediction using Logistic Regression  
- Interactive dashboard for business users  
- Clear separation of database, analysis, and presentation layers  


## Dashboard Overview

The Streamlit dashboard displays:
- Total customers  
- Number of churned customers  
- Retention rate  
- Churn distribution  
- List of high-risk customers  

This enables non-technical users to interpret results easily.


## How to Run the Project

1. Create the database using `database/schema.sql`  
2. Update database credentials in the code using placeholders or environment variables  
3. Run the analysis script if required  

```bash
python python/analysis.py
```

4. Launch the Streamlit dashboard  

```bash
python -m streamlit run frontend/app.py
```
 

## Important Note

This project uses a small sample dataset for demonstration purposes.  
The goal is to showcase an end-to-end data science workflow rather than production-level accuracy.


## Future Improvements

- Larger and more realistic datasets  
- Advanced churn modeling techniques  
- Secure credential handling using environment variables  
- Cloud deployment  


## Author

Nidhin  
Aspiring Data Scientist and AI/ML Enthusiast
