/*
=========================================================
FILE: 03_loan_credit_analysis.sql
PROJECT: Finance Customer Risk & Profitability Analytics
PURPOSE: Analyze loan exposure and credit-card behavior
=========================================================

TABLE OF CONTENTS
-----------------
1. Loan Type Distribution
2. Loan Exposure by Type
3. Loan Status Analysis
4. Average Interest Rate by Loan Type
5. Loan Term Analysis
6. Credit Card Type Analysis
7. Credit Utilization
8. High Credit Utilization Customers
9. Credit Exposure by Card Type
=========================================================
*/


/* =====================================================
   1. LOAN TYPE DISTRIBUTION
   ===================================================== */

SELECT
    Loan_Type,
    COUNT(*) AS Loan_Count
FROM banking_features
GROUP BY Loan_Type
ORDER BY Loan_Count DESC;


/* =====================================================
   2. LOAN EXPOSURE BY TYPE
   ===================================================== */

SELECT
    Loan_Type,
    COUNT(*) AS Loan_Count,
    ROUND(AVG(Loan_Amount), 2) AS Avg_Loan_Amount,
    ROUND(SUM(Loan_Amount), 2) AS Total_Loan_Exposure
FROM banking_features
GROUP BY Loan_Type
ORDER BY Total_Loan_Exposure DESC;


/* =====================================================
   3. LOAN STATUS ANALYSIS
   ===================================================== */

SELECT
    Loan_Status,
    COUNT(*) AS Customer_Count,
    ROUND(AVG(Loan_Amount), 2) AS Avg_Loan_Amount
FROM banking_features
GROUP BY Loan_Status
ORDER BY Customer_Count DESC;


/* =====================================================
   4. AVERAGE INTEREST RATE BY LOAN TYPE
   ===================================================== */

SELECT
    Loan_Type,
    ROUND(AVG(Interest_Rate), 2) AS Avg_Interest_Rate
FROM banking_features
GROUP BY Loan_Type
ORDER BY Avg_Interest_Rate DESC;


/* =====================================================
   5. LOAN TERM ANALYSIS
   ===================================================== */

SELECT
    Loan_Type,
    ROUND(AVG(Loan_Term), 2) AS Avg_Loan_Term,
    MIN(Loan_Term) AS Min_Loan_Term,
    MAX(Loan_Term) AS Max_Loan_Term
FROM banking_features
GROUP BY Loan_Type
ORDER BY Avg_Loan_Term DESC;


/* =====================================================
   6. CREDIT CARD TYPE ANALYSIS
   ===================================================== */

SELECT
    Card_Type,
    COUNT(*) AS Card_Count,
    ROUND(AVG(Credit_Limit), 2) AS Avg_Credit_Limit,
    ROUND(AVG(Credit_Card_Balance), 2) AS Avg_Card_Balance
FROM banking_features
GROUP BY Card_Type
ORDER BY Avg_Credit_Limit DESC;


/* =====================================================
   7. CREDIT UTILIZATION
   ===================================================== */

SELECT
    Customer_ID,
    Credit_Limit,
    Credit_Card_Balance,

    ROUND(
        (Credit_Card_Balance / NULLIF(Credit_Limit, 0)) * 100,
        2
    ) AS Credit_Utilization_Pct

FROM banking_features
ORDER BY Credit_Utilization_Pct DESC;


/* =====================================================
   8. HIGH CREDIT UTILIZATION CUSTOMERS
   ===================================================== */

SELECT
    Customer_ID,
    Credit_Limit,
    Credit_Card_Balance,

    ROUND(
        (Credit_Card_Balance / NULLIF(Credit_Limit, 0)) * 100,
        2
    ) AS Credit_Utilization_Pct

FROM banking_features

WHERE
    (Credit_Card_Balance / NULLIF(Credit_Limit, 0)) * 100 >= 70

ORDER BY Credit_Utilization_Pct DESC;


/* =====================================================
   9. CREDIT EXPOSURE BY CARD TYPE
   ===================================================== */

SELECT
    Card_Type,
    COUNT(*) AS Customer_Count,
    ROUND(SUM(Credit_Limit), 2) AS Total_Credit_Limit,
    ROUND(SUM(Credit_Card_Balance), 2) AS Total_Card_Balance
FROM banking_features
GROUP BY Card_Type
ORDER BY Total_Credit_Limit DESC;