DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS usage_logs;
DROP TABLE IF EXISTS subscriptions;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    region VARCHAR(50),
    signup_date DATE
);

CREATE TABLE subscriptions (
    subscription_id INT PRIMARY KEY,
    customer_id INT,
    plan_type VARCHAR(50),
    start_date DATE,
    end_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE usage_logs (
    usage_id INT PRIMARY KEY,
    customer_id INT,
    login_date DATE,
    session_minutes INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    customer_id INT,
    payment_date DATE,
    amount DECIMAL(10,2),
    payment_status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
