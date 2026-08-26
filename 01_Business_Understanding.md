# Business Understanding
## Finance Customer Risk & Profitability Analytics

---

## 1. Project Title

**Finance Customer Risk & Profitability Analytics**

## 2. Business Domain

Banking / Consumer Finance

## 3. Role

Data Analyst

## 4. Tools

Python + SQL

## 5. Dataset Overview

The analysis is built on the **Comprehensive Banking Database**, a single wide table combining customer, account, transaction, loan, credit card, and feedback data.

| Property | Value |
|---|---|
| Records | 5,000 rows (5,000 unique customers, one row per customer) |
| Columns | 40 |
| Grain | One row = one customer, joined with their most recent/associated transaction, loan, card, and feedback record |
| Missing values | None detected across all 40 columns |

**Column groups:**

| Domain | Fields |
|---|---|
| Customer profile | Customer ID, First Name, Last Name, Age, Gender, Address, City, Contact Number, Email |
| Account | Account Type, Account Balance, Date Of Account Opening, Last Transaction Date |
| Transactions | TransactionID, Transaction Date, Transaction Type, Transaction Amount, Account Balance After Transaction, Branch ID |
| Loans | Loan ID, Loan Amount, Loan Type, Interest Rate, Loan Term, Approval/Rejection Date, Loan Status |
| Credit Cards | CardID, Card Type, Credit Limit, Credit Card Balance, Minimum Payment Due, Payment Due Date, Last Credit Card Payment Date, Rewards Points |
| Feedback / Service | Feedback ID, Feedback Date, Feedback Type, Resolution Status, Resolution Date |
| Risk Flag | Anomaly |

**Key categorical distributions (roughly balanced, ~1/3 or ~1/2 splits — good for segmentation and hypothesis testing):**

- Account Type: Savings (2,507) / Current (2,493)
- Loan Type: Mortgage (1,712) / Auto (1,645) / Personal (1,643)
- Loan Status: Approved (1,710) / Closed (1,660) / Rejected (1,630)
- Card Type: MasterCard (1,696) / AMEX (1,679) / Visa (1,625)
- Transaction Type: Deposit (1,698) / Withdrawal (1,673) / Transfer (1,629)
- Feedback Type: Suggestion (1,689) / Complaint (1,681) / Praise (1,630)
- Resolution Status: Pending (2,504) / Resolved (2,496)
- **Anomaly**: Normal = 1 (4,700 customers) / Flagged = -1 (300 customers, ~6% of the portfolio)

**Numeric ranges:**

- Age: 18–69
- Account Balance: ~$107 – $9,998 (mean ≈ $5,061)
- Loan Amount: ~$1,006 – $49,993 (mean ≈ $25,501)
- Transaction Amount: ~$11 – $4,998 (mean ≈ $2,509)
- Credit Card Balance: ~$1 – $4,997 (mean ≈ $2,487)
- 40 cities represented across the customer base

---

## 6. Business Problem Statement

> A financial services company wants to understand its customer portfolio, financial exposure, credit behavior, and customer value. The objective is to identify valuable customer segments, detect potential financial risk, understand the factors associated with risk, and provide data-driven recommendations for improving customer value while managing risk.

The bank currently holds rich transactional, credit, and service data on 5,000 customers but has no unified view that connects **who its customers are**, **how much value they generate**, **how risky they are**, and **what the business should do about each group**. This project builds that view.

---

## 7. Core Business Questions

The project is scoped around four focused business questions, each mapped directly to fields available in the dataset.

### Question 1 — Customer & Portfolio Performance
**What does the company's customer and financial portfolio look like?**

Analyze:
- Customer demographics (Age, Gender, City)
- Account types and balances (Account Type, Account Balance)
- Transaction behavior (Transaction Type, Transaction Amount, Account Balance After Transaction)
- Loan portfolio composition (Loan Type, Loan Amount, Loan Status, Interest Rate, Loan Term)
- Credit card portfolio (Card Type, Credit Limit, Credit Card Balance, Rewards Points)

### Question 2 — Customer Value & Segmentation
**Which customers are most valuable, and what characteristics distinguish different customer segments?**

Use:
- Feature engineering (e.g., Credit Utilization %, Transaction-to-Balance Ratio, Loan Exposure, Customer Value Score)
- Descriptive statistics on engineered features
- Business-rule customer segmentation (Value × Risk matrix)

### Question 3 — Credit Risk
**Which customer and financial characteristics are associated with higher risk?**

Analyze:
- Loan Status, Loan Amount, Interest Rate
- Credit Utilization (Credit Card Balance ÷ Credit Limit)
- Payment behavior (Minimum Payment Due, Payment Due Date vs Last Credit Card Payment Date)
- Account Balance
- The **Anomaly** flag (pre-labeled irregular accounts — a natural validation target for the risk score)

Use:
- Distribution and outlier analysis (IQR, boxplots)
- Correlation analysis
- Hypothesis testing (e.g., t-test / Mann–Whitney U comparing credit utilization between flagged vs. normal customers)
- Chi-square (e.g., is Loan Type associated with Loan Status? Is Feedback Type associated with Resolution Status?)
- Business-rule risk scoring (Low / Medium / High)

### Question 4 — Profitability vs. Risk
**Which customer groups should the company retain, grow, monitor, or review?**

Combine **Customer Value** and **Financial Risk** into a single decision framework:

```text
                 RISK
             Low         High
VALUE High   Grow        Monitor
     Low     Develop     Review
```

This is the main business decision section of the project — translating analytics into a clear action for each customer segment.

---

## 8. Planned Analytical Toolkit

| Method | Priority | Purpose |
|---|---|---|
| Descriptive statistics | Must have | Summarize balances, loans, transactions, utilization |
| Distribution & outlier analysis | Must have | Flag unusually high loans, balances, transactions |
| Feature engineering | Must have | Build Credit Utilization %, Payment Delay, Loan Exposure, Value Score |
| Customer segmentation | Must have | Business-rule Value × Risk quadrant |
| Correlation analysis | Recommended | Test relationships, e.g., utilization vs. delay |
| Hypothesis testing | Recommended | Statistically validate risk differences between groups |
| Chi-square | Optional | Test associations between categorical variables |
| Risk scoring | Must have | Transparent Low/Medium/High risk classification |
| Profitability / customer value analysis | Must have | Core business output — value vs. risk |

**SQL** will handle aggregation, `GROUP BY`, `CASE`, `JOIN`, CTEs, subqueries, window functions, date functions, and ranking — primarily for building the customer-level summary tables that feed the Python analysis.

Deliberately out of scope: PCA, time-series forecasting, deep learning, random forests, neural networks, exhaustive clustering algorithms, ANOVA without a clear question, and advanced econometrics. These would broaden the project without adding proportional business value.

---

## 9. Expected Final Output

The project should ultimately answer:

1. **Who are our most valuable customers?**
2. **Who presents the greatest financial risk?**
3. **What characteristics differentiate them?**
4. **Is there a measurable relationship between customer value and risk?**
5. **What should the company do based on these findings?**

## 10. Project Narrative

**Business problem → Data cleaning → Finance metrics → Descriptive analysis → Risk analysis → Segmentation → Statistical validation → Profitability → Business recommendations**

## 11. Project Folder Structure

```text
Finance_Customer_Risk_Analytics/
│
├── data/
├── python/
├── sql/
├── outputs/
└── README.md
```
