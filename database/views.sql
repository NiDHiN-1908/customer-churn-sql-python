-- Remove old view if exists
DROP VIEW IF EXISTS churn_features;

-- Feature view used by ML pipeline
CREATE VIEW churn_features AS
SELECT
    tenure,
    age,
    income,
    longmon,
    tollmon,
    wiremon,
    cardmon,
    churn
FROM telco_customers;
