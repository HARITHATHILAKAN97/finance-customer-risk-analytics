/*
=========================================================
FILE: 01_basic_portfolio_analysis.sql
PROJECT: Finance Customer Risk & Profitability Analytics
PURPOSE: Understand the overall customer and financial portfolio
=========================================================

TABLE OF CONTENTS
-----------------
1. Total Customers
2. Customers by Account Type
3. Average Account Balance by Account Type
4. Overall Account Balance Statistics
5. Transaction Portfolio
6. Loan Portfolio
7. Loan Status Distribution
8. Credit Card Portfolio
9. City-Level Portfolio
=========================================================
*/


/* =====================================================
   1. TOTAL CUSTOMERS
   ===================================================== */

SELECT
    COUNT(*) AS Total_Customers
FROM banking_features;


/* =====================================================
   2. CUSTOMERS BY ACCOUNT TYPE
   ===================================================== */

SELECT
    Account_Type,
    COUNT(*) AS Customer_Count
FROM banking_features
GROUP BY Account_Type
ORDER BY Customer_Count DESC;


/* =====================================================
   3. AVERAGE ACCOUNT BALANCE BY ACCOUNT TYPE
   ===================================================== */

SELECT
    Account_Type,
    COUNT(*) AS Customer_Count,
    ROUND(AVG(Account_Balance), 2) AS Avg_Account_Balance
FROM banking_features
GROUP BY Account_Type
ORDER BY Avg_Account_Balance DESC;


/* =====================================================
   4. OVERALL ACCOUNT BALANCE STATISTICS
   ===================================================== */

SELECT
    COUNT(*) AS Customers,
    ROUND(AVG(Account_Balance), 2) AS Avg_Balance,
    ROUND(MIN(Account_Balance), 2) AS Min_Balance,
    ROUND(MAX(Account_Balance), 2) AS Max_Balance
FROM banking_features;


/* =====================================================
   5. TRANSACTION PORTFOLIO
   ===================================================== */

SELECT
    Transaction_Type,
    COUNT(*) AS Transaction_Count,
    ROUND(AVG(Transaction_Amount), 2) AS Avg_Transaction_Amount,
    ROUND(SUM(Transaction_Amount), 2) AS Total_Transaction_Amount
FROM banking_features
GROUP BY Transaction_Type
ORDER BY Total_Transaction_Amount DESC;


/* =====================================================
   6. LOAN PORTFOLIO
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
   7. LOAN STATUS DISTRIBUTION
   ===================================================== */

SELECT
    Loan_Status,
    COUNT(*) AS Customer_Count,
    ROUND(AVG(Loan_Amount), 2) AS Avg_Loan_Amount
FROM banking_features
GROUP BY Loan_Status
ORDER BY Customer_Count DESC;


/* =====================================================
   8. CREDIT CARD PORTFOLIO
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
   9. CITY-LEVEL PORTFOLIO
   ===================================================== */

SELECT
    City,
    COUNT(*) AS Customer_Count,
    ROUND(AVG(Account_Balance), 2) AS Avg_Account_Balance
FROM banking_features
GROUP BY City
ORDER BY Customer_Count DESC;


