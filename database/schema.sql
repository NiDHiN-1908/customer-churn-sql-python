-- Drop table if it already exists (for clean reset)
DROP TABLE IF EXISTS telco_customers;

-- Main table to store customer behavioral data
CREATE TABLE telco_customers (
    tenure FLOAT,       -- Number of months the customer stayed
    age FLOAT,
    address FLOAT,
    income FLOAT,
    ed FLOAT,           -- Education level
    employ FLOAT,       -- Years employed
    equip FLOAT,        -- Equipment count
    callcard FLOAT,
    wireless FLOAT,
    longmon FLOAT,     -- Monthly long distance charges
    tollmon FLOAT,     -- Monthly toll charges
    equipmon FLOAT,
    cardmon FLOAT,
    wiremon FLOAT,
    longten FLOAT,     -- Total long distance usage
    tollten FLOAT,
    cardten FLOAT,
    voice FLOAT,
    pager FLOAT,
    internet FLOAT,
    callwait FLOAT,
    confer FLOAT,
    ebill FLOAT,
    loglong FLOAT,
    logtoll FLOAT,
    lninc FLOAT,
    custcat FLOAT,
    churn FLOAT         -- Target variable (1 = churn, 0 = retain)
);
