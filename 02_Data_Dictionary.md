# Data Dictionary
## Comprehensive Banking Database

**Source file:** `Comprehensive_Banking_Database.csv`
**Rows:** 5,000 (one row per customer)
**Columns:** 40
**Missing values:** None across any column

---

## 1. Customer Profile

| Column | Type | Unique Values | Description | Example |
|---|---|---|---|---|
| Customer ID | Integer | 5,000 (all unique) | Primary key uniquely identifying each customer | 1 |
| First Name | Text | 50 | Customer's first name | Joshua |
| Last Name | Text | 50 | Customer's last name | Hall |
| Age | Integer | 52 (range 18–69) | Customer's age in years | 45 |
| Gender | Categorical | 3 (Male / Female / Other) | Customer's gender | Male |
| Address | Text | 5,000 (all unique) | Street address identifier | Address_1 |
| City | Categorical | 40 | City of residence | Fort Worth |
| Contact Number | Integer | 5,000 (all unique) | Customer phone number | 19458794854 |
| Email | Text | 2,139 | Customer email address (some shared across customers) | joshua.hall@kag.com |

## 2. Account Information

| Column | Type | Unique Values | Description | Example |
|---|---|---|---|---|
| Account Type | Categorical | 2 (Savings / Current) | Type of bank account held | Current |
| Account Balance | Float | 4,991 (range ~$107–$9,998) | Current balance in the account (USD) | 1313.38 |
| Date Of Account Opening | Date (string, M/D/YYYY) | 3,738 | Date the account was opened | 5/26/2006 |
| Last Transaction Date | Date (string, M/D/YYYY) | 365 | Date of the customer's most recent transaction | 4/23/2023 |

## 3. Transaction Details

| Column | Type | Unique Values | Description | Example |
|---|---|---|---|---|
| TransactionID | Integer | 5,000 (all unique) | Unique identifier for the transaction record | 1 |
| Transaction Date | Date (string, M/D/YYYY) | 365 | Date the transaction occurred | 12/7/2023 |
| Transaction Type | Categorical | 3 (Deposit / Withdrawal / Transfer) | Nature of the transaction | Withdrawal |
| Transaction Amount | Float | 4,972 (range ~$11–$4,998) | Dollar amount of the transaction (USD) | 1457.61 |
| Account Balance After Transaction | Float | 4,984 | Account balance immediately following the transaction (USD) | 2770.99 |
| Branch ID | Integer | 99 (range 1–99) | Identifier of the branch where the transaction occurred | 43 |

## 4. Loan Details

| Column | Type | Unique Values | Description | Example |
|---|---|---|---|---|
| Loan ID | Integer | 5,000 (all unique) | Unique identifier for the loan record | 1 |
| Loan Amount | Float | 5,000 (all unique, range ~$1,006–$49,993) | Principal amount of the loan (USD) | 32200.06 |
| Loan Type | Categorical | 3 (Mortgage / Auto / Personal) | Category of loan product | Mortgage |
| Interest Rate | Float | 900 (range 1.0%–10.0%) | Annual interest rate applied to the loan | 2.64 |
| Loan Term | Integer | 5 (12 / 24 / 36 / 48 / 60 months) | Loan repayment term, in months | 36 |
| Approval/Rejection Date | Date (string, M/D/YYYY) | 1,088 | Date the loan decision was made | 5/11/2021 |
| Loan Status | Categorical | 3 (Approved / Rejected / Closed) | Current status of the loan application/account | Rejected |

## 5. Credit Card Details

| Column | Type | Unique Values | Description | Example |
|---|---|---|---|---|
| CardID | Integer | 5,000 (all unique) | Unique identifier for the credit card record | 1 |
| Card Type | Categorical | 3 (AMEX / MasterCard / Visa) | Credit card network/brand | AMEX |
| Credit Limit | Float | 4,992 (range ~$1,007–$9,998) | Maximum credit limit assigned to the card (USD) | 1737.88 |
| Credit Card Balance | Float | 4,965 (range ~$1–$4,997) | Current outstanding balance on the card (USD) | 4524.32 |
| Minimum Payment Due | Float | 4,523 (range ~$0.07–$249.86) | Minimum payment required by the due date (USD) | 226.22 |
| Payment Due Date | Date (string, M/D/YYYY) | 365 | Date the minimum payment is due | 11/26/2023 |
| Last Credit Card Payment Date | Date (string, M/D/YYYY) | 365 | Date the customer last made a credit card payment | 3/20/2023 |
| Rewards Points | Integer | 3,948 (range 1–9,999) | Accumulated rewards/loyalty points on the card | 8142 |

## 6. Feedback / Customer Service

| Column | Type | Unique Values | Description | Example |
|---|---|---|---|---|
| Feedback ID | Integer | 5,000 (all unique) | Unique identifier for the feedback record | 1 |
| Feedback Date | Date (string, M/D/YYYY) | 365 | Date the feedback was submitted | 10/6/2023 |
| Feedback Type | Categorical | 3 (Suggestion / Complaint / Praise) | Category of customer feedback | Suggestion |
| Resolution Status | Categorical | 2 (Resolved / Pending) | Whether the feedback has been resolved | Resolved |
| Resolution Date | Date (string, M/D/YYYY) | 365 | Date the feedback was resolved (if applicable) | 1/22/2023 |

## 7. Risk Flag

| Column | Type | Unique Values | Description | Example |
|---|---|---|---|---|
| Anomaly | Integer | 2 (1 / -1) | Pre-labeled anomaly indicator: **1 = Normal** (4,700 customers), **-1 = Flagged/Anomalous** (300 customers, ~6% of the base) | 1 |

---


