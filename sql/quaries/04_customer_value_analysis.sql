/*
=========================================================
FILE: 04_customer_value_analysis.sql
PROJECT: Finance Customer Risk & Profitability Analytics
PURPOSE: Identify and rank financially valuable customers
=========================================================

TABLE OF CONTENTS
-----------------
1. Customer Financial Profile
2. Customer Value Score
3. Value Categories
4. High-Value Customers
5. Value Category Summary
=========================================================
*/


/* =====================================================
   1. CUSTOMER FINANCIAL PROFILE
   ===================================================== */

SELECT
    Customer_ID,
    Account_Balance,
    Loan_Amount,
    Transaction_Amount,
    Credit_Card_Balance
FROM banking_features;


/* =====================================================
   2. CUSTOMER VALUE SCORE
   ===================================================== */

SELECT
    Customer_ID,
    Account_Balance,
    Transaction_Amount,
    Loan_Amount,

    (
        Account_Balance
        + Transaction_Amount
        + Loan_Amount
    ) AS Customer_Value_Score

FROM banking_features

ORDER BY Customer_Value_Score DESC;


/* =====================================================
   3. VALUE CATEGORIES
   ===================================================== */

SELECT
    Customer_ID,
    Account_Balance,

    CASE
        WHEN Account_Balance >= 7500
            THEN 'High Value'

        WHEN Account_Balance >= 4000
            THEN 'Medium Value'

        ELSE 'Low Value'
    END AS Value_Category

FROM banking_features;


/* =====================================================
   4. HIGH-VALUE CUSTOMERS
   ===================================================== */

SELECT TOP 10
    Customer_ID,
    Account_Balance,
    Loan_Amount,
    Transaction_Amount,
    Credit_Card_Balance

FROM banking_features

ORDER BY Account_Balance DESC;


/* =====================================================
   5. VALUE CATEGORY SUMMARY
   ===================================================== */

SELECT

    CASE
        WHEN Account_Balance >= 7500
            THEN 'High Value'

        WHEN Account_Balance >= 4000
            THEN 'Medium Value'

        ELSE 'Low Value'
    END AS Value_Category,

    COUNT(*) AS Customer_Count,

    ROUND(AVG(Account_Balance), 2)
        AS Avg_Account_Balance,

    ROUND(AVG(Loan_Amount), 2)
        AS Avg_Loan_Amount,

    ROUND(AVG(Transaction_Amount), 2)
        AS Avg_Transaction_Amount

FROM banking_features

GROUP BY

    CASE
        WHEN Account_Balance >= 7500
            THEN 'High Value'

        WHEN Account_Balance >= 4000
            THEN 'Medium Value'

        ELSE 'Low Value'
    END

ORDER BY Avg_Account_Balance DESC;