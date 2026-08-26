/*
=========================================================
FILE: 05_customer_metrics.sql
PROJECT: Finance Customer Risk & Profitability Analytics
PURPOSE: Create customer-level analytical metrics
=========================================================

TABLE OF CONTENTS
-----------------
1. Credit Utilization
2. Loan Exposure
3. Transaction-to-Balance Ratio
4. Anomaly Distribution
5. Customer Risk Indicators
=========================================================
*/


/* =====================================================
   1. CREDIT UTILIZATION
   ===================================================== */

SELECT
    Customer_ID,

    ROUND(
        (Credit_Card_Balance / NULLIF(Credit_Limit, 0)) * 100,
        2
    ) AS Credit_Utilization_Pct

FROM banking_features;


/* =====================================================
   2. LOAN EXPOSURE
   ===================================================== */

SELECT
    Customer_ID,
    Loan_Amount,
    Account_Balance,

    ROUND(
        Loan_Amount / NULLIF(Account_Balance, 0),
        2
    ) AS Loan_to_Balance_Ratio

FROM banking_features;


/* =====================================================
   3. TRANSACTION-TO-BALANCE RATIO
   ===================================================== */

SELECT
    Customer_ID,
    Transaction_Amount,
    Account_Balance,

    ROUND(
        Transaction_Amount / NULLIF(Account_Balance, 0),
        2
    ) AS Transaction_to_Balance_Ratio

FROM banking_features;


/* =====================================================
   4. ANOMALY DISTRIBUTION
   ===================================================== */

SELECT
    Anomaly,
    COUNT(*) AS Customer_Count
FROM banking_features
GROUP BY Anomaly
ORDER BY Customer_Count DESC;


/* =====================================================
   5. CUSTOMER RISK INDICATORS
   ===================================================== */

SELECT
    Customer_ID,
    Account_Balance,
    Loan_Amount,
    Credit_Limit,
    Credit_Card_Balance,
    Anomaly,

    ROUND(
        (Credit_Card_Balance / NULLIF(Credit_Limit, 0)) * 100,
        2
    ) AS Credit_Utilization_Pct,

    CASE
        WHEN Anomaly = -1
            THEN 'High Risk'

        WHEN
            (Credit_Card_Balance /
             NULLIF(Credit_Limit, 0)) * 100 >= 70
            THEN 'Medium Risk'

        ELSE 'Low Risk'
    END AS Risk_Category

FROM banking_features;