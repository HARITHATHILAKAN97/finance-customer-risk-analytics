/*
=========================================================
FILE: 06_value_risk_analysis.sql
PROJECT: Finance Customer Risk & Profitability Analytics
PURPOSE: Combine customer value and risk into business segments
=========================================================

TABLE OF CONTENTS
-----------------
1. Customer Value + Risk Analysis
2. Customer Ranking
3. Value × Risk Segmentation
4. Business Action Assignment
5. Value × Risk Summary
=========================================================
*/


/* =====================================================
   1. CUSTOMER VALUE + RISK ANALYSIS
   ===================================================== */

WITH Customer_Analysis AS
(
    SELECT

        Customer_ID,
        City,
        Account_Balance,
        Loan_Amount,
        Credit_Limit,
        Credit_Card_Balance,
        Anomaly,

        ROUND(
            (Credit_Card_Balance /
             NULLIF(Credit_Limit, 0)) * 100,
            2
        ) AS Credit_Utilization_Pct,

        RANK() OVER
        (
            ORDER BY Account_Balance DESC
        ) AS Balance_Rank,

        CASE

            WHEN Account_Balance >= 7500
                THEN 'High Value'

            WHEN Account_Balance >= 4000
                THEN 'Medium Value'

            ELSE 'Low Value'

        END AS Value_Category,

        CASE

            WHEN Anomaly = -1
                THEN 'High Risk'

            ELSE 'Normal'

        END AS Risk_Category

    FROM banking_features
)

SELECT

    Customer_ID,
    City,
    Account_Balance,
    Loan_Amount,
    Credit_Utilization_Pct,
    Balance_Rank,
    Value_Category,
    Risk_Category,

    CASE

        WHEN Value_Category = 'High Value'
             AND Risk_Category = 'Normal'
            THEN 'Grow'

        WHEN Value_Category = 'High Value'
             AND Risk_Category = 'High Risk'
            THEN 'Monitor'

        WHEN Value_Category IN
             ('Medium Value', 'Low Value')
             AND Risk_Category = 'Normal'
            THEN 'Develop'

        WHEN Value_Category IN
             ('Medium Value', 'Low Value')
             AND Risk_Category = 'High Risk'
            THEN 'Review'

    END AS Business_Action

FROM Customer_Analysis

ORDER BY Balance_Rank;


/* =====================================================
   2. VALUE × RISK SUMMARY
   ===================================================== */

WITH Customer_Analysis AS
(
    SELECT

        Customer_ID,
        Account_Balance,
        Loan_Amount,
        Credit_Limit,
        Credit_Card_Balance,
        Anomaly,

        ROUND(
            (Credit_Card_Balance /
             NULLIF(Credit_Limit, 0)) * 100,
            2
        ) AS Credit_Utilization_Pct,

        CASE

            WHEN Account_Balance >= 7500
                THEN 'High Value'

            WHEN Account_Balance >= 4000
                THEN 'Medium Value'

            ELSE 'Low Value'

        END AS Value_Category,

        CASE

            WHEN Anomaly = -1
                THEN 'High Risk'

            ELSE 'Normal'

        END AS Risk_Category

    FROM banking_features
)

SELECT

    Value_Category,
    Risk_Category,

    COUNT(*) AS Customer_Count,

    ROUND(
        AVG(Account_Balance),
        2
    ) AS Avg_Account_Balance,

    ROUND(
        AVG(Loan_Amount),
        2
    ) AS Avg_Loan_Amount,

    ROUND(
        AVG(Credit_Utilization_Pct),
        2
    ) AS Avg_Credit_Utilization,

    CASE

        WHEN Value_Category = 'High Value'
             AND Risk_Category = 'Normal'
            THEN 'Grow'

        WHEN Value_Category = 'High Value'
             AND Risk_Category = 'High Risk'
            THEN 'Monitor'

        WHEN Value_Category IN
             ('Medium Value', 'Low Value')
             AND Risk_Category = 'Normal'
            THEN 'Develop'

        WHEN Value_Category IN
             ('Medium Value', 'Low Value')
             AND Risk_Category = 'High Risk'
            THEN 'Review'

    END AS Business_Action

FROM Customer_Analysis

GROUP BY
    Value_Category,
    Risk_Category

ORDER BY
    Value_Category,
    Risk_Category;


/* =====================================================
   3. TOP 10 HIGH-VALUE CUSTOMERS
   ===================================================== */

SELECT TOP 10

    Customer_ID,
    Account_Balance,
    Loan_Amount,
    Credit_Card_Balance,
    Anomaly

FROM banking_features

ORDER BY Account_Balance DESC;


/* =====================================================
   4. FINAL DATA VALIDATION
   ===================================================== */

SELECT

    COUNT(*) AS Total_Rows,

    COUNT(DISTINCT Customer_ID)
        AS Unique_Customers

FROM banking_features;


/* =====================================================
   5. ANOMALY VALIDATION
   ===================================================== */

SELECT

    Anomaly,
    COUNT(*) AS Customer_Count

FROM banking_features

GROUP BY Anomaly

ORDER BY Customer_Count DESC;