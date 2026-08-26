/*
=========================================================
FILE: 02_account_transaction_analysis.sql
PROJECT: Finance Customer Risk & Profitability Analytics
PURPOSE: Analyze account balances and transaction behavior
=========================================================

TABLE OF CONTENTS
-----------------
1. Account Type Distribution
2. Account Balance by Account Type
3. Transaction Type Distribution
4. Transaction Amount by Transaction Type
5. Account Balance After Transaction
6. Transaction Activity by City
7. Highest Transaction Customers
=========================================================
*/


/* =====================================================
   1. ACCOUNT TYPE DISTRIBUTION
   ===================================================== */

SELECT
    Account_Type,
    COUNT(*) AS Customer_Count
FROM banking_features
GROUP BY Account_Type
ORDER BY Customer_Count DESC;


/* =====================================================
   2. ACCOUNT BALANCE BY ACCOUNT TYPE
   ===================================================== */

SELECT
    Account_Type,
    COUNT(*) AS Customer_Count,
    ROUND(AVG(Account_Balance), 2) AS Avg_Account_Balance,
    ROUND(MIN(Account_Balance), 2) AS Min_Account_Balance,
    ROUND(MAX(Account_Balance), 2) AS Max_Account_Balance
FROM banking_features
GROUP BY Account_Type
ORDER BY Avg_Account_Balance DESC;


/* =====================================================
   3. TRANSACTION TYPE DISTRIBUTION
   ===================================================== */

SELECT
    Transaction_Type,
    COUNT(*) AS Transaction_Count
FROM banking_features
GROUP BY Transaction_Type
ORDER BY Transaction_Count DESC;


/* =====================================================
   4. TRANSACTION AMOUNT BY TRANSACTION TYPE
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
   5. ACCOUNT BALANCE AFTER TRANSACTION
   ===================================================== */

SELECT
    Transaction_Type,
    ROUND(AVG(Account_Balance_After_Transaction), 2)
        AS Avg_Balance_After_Transaction,
    ROUND(MIN(Account_Balance_After_Transaction), 2)
        AS Min_Balance_After_Transaction,
    ROUND(MAX(Account_Balance_After_Transaction), 2)
        AS Max_Balance_After_Transaction
FROM banking_features
GROUP BY Transaction_Type
ORDER BY Avg_Balance_After_Transaction DESC;


/* =====================================================
   6. TRANSACTION ACTIVITY BY CITY
   ===================================================== */

SELECT
    City,
    COUNT(*) AS Customer_Count,
    ROUND(AVG(Transaction_Amount), 2)
        AS Avg_Transaction_Amount,
    ROUND(SUM(Transaction_Amount), 2)
        AS Total_Transaction_Amount
FROM banking_features
GROUP BY City
ORDER BY Total_Transaction_Amount DESC;


/* =====================================================
   7. HIGHEST TRANSACTION CUSTOMERS
   ===================================================== */

SELECT TOP 10
    Customer_ID,
    Transaction_Amount,
    Transaction_Type,
    Account_Balance
FROM banking_features
ORDER BY Transaction_Amount DESC;