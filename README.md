Finance Customer Risk & Profitability Analytics

End-to-end SQL + Python analytics project on a 5,000-customer banking dataset — from raw data to a business-ready Value × Risk segmentation and a set of data-driven recommendations.

Domain: Banking / Consumer Finance · Role: Data Analyst · Tools: SQL, Python (pandas, matplotlib)

📌 Business Problem

A financial services company has rich transactional, credit, and service data on its customers but no unified view connecting who its customers are, how much value they generate, how risky they are, and what the business should do about each group. This project builds that view — segmenting customers into a Value × Risk framework and translating the analysis into concrete business actions.

Core business questions:

What does the customer and financial portfolio look like?
Which customers are most valuable, and what distinguishes different segments?
Which characteristics are associated with higher credit risk?
Which customer groups should the company retain, grow, monitor, or review?
🗂️ Dataset

The Comprehensive Banking Database — one row per customer, joined with each customer's most recent transaction, loan, credit card, and feedback record.

Property	Value
Records	5,000 customers
Source columns	40
Missing values	None detected
Domains covered	Customer profile, Account, Transactions, Loans, Credit Cards, Feedback/Service, Anomaly (risk) flag

Key numeric ranges: Account Balance $107–$9,998 · Loan Amount $1,006–$49,993 · Credit Card Balance $1–$4,997 · Age 18–69.

🧱 Project Structure
Finance_Customer_Risk_Analytics/
│
├── data/
│   ├── raw/                  # Original source data
│   ├── cleaned/               # Cleaned dataset (data_cleaning.py output)
│   └── processed/             # Feature-engineered dataset (feature_engineering.py output)
│
├── python/
│   ├── data_inspection.py     # 01 — initial structural inspection
│   ├── data_quality_check.py  # 02 — PASS/REVIEW data quality checks
│   ├── data_cleaning.py       # 03 — cleaning, standardization, type conversion
│   ├── feature_engineering.py # 04 — builds the analytical feature set
│   ├── eda.py                 # 05 — exploratory data analysis + visualizations
│   └── report/                # Auto-generated text reports from each script
│
├── sql/
│   ├── 01_basic_portfolio_analysis.sql
│   ├── 02_account_transaction_analysis.sql
│   ├── 03_loan_credit_analysis.sql
│   ├── 04_customer_value_analysis.sql
│   ├── 05_customer_metrics.sql
│   └── 06_value_risk_analysis.sql
│
├── outputs/
│   └── eda/                   # 8 saved chart images (.png)
│
├── docs/
│   ├── business_understanding.md
│   ├── data_dictionary.md
│   └── business_insights.md   # Full findings & recommendations
│
└── README.md
🔧 Methodology

Pipeline: Business problem → Data cleaning → Feature engineering → Descriptive analysis → Risk analysis → Segmentation → Statistical validation → Profitability → Business recommendations

Method	Purpose
Descriptive statistics	Summarize balances, loans, transactions, utilization
Distribution & outlier analysis	Flag unusually high loans, balances, transactions
Feature engineering	Credit Utilization %, Loan-to-Balance Ratio, Risk Score, Customer Value Score
Customer segmentation	Business-rule Value × Risk quadrant
Correlation analysis	Test relationships (e.g., utilization vs. risk)
Hypothesis testing / Chi-square	Statistically validate risk & categorical associations
Risk scoring	Transparent Low / Medium / High classification
Profitability analysis	Core output — customer value vs. risk

Engineered features include: Age Group, Account Age Years, Transaction Recency Days, Credit Utilization %, Available Credit, Loan-to-Balance Ratio, Payment Timing Days, Complaint/Pending Feedback Flags, Risk Score, Risk Level, Customer Value Score, Customer Value Segment, and Value Risk Segment (Grow / Monitor / Develop / Review).

Deliberately out of scope: PCA, time-series forecasting, deep learning, random forests, neural networks, exhaustive clustering, and advanced econometrics — kept out to match the project's business scope.

📊 Key Findings
Value is concentrated: 20.3% of customers are High Value (avg. balance ~$8,214) vs. 17.8% Low Value (avg. balance ~$1,734).
Risk is broader than the raw anomaly flag suggests: 14.3% High Risk by the business-rule score vs. only 6.0% flagged by the original Anomaly column.
Credit utilization is the strongest risk driver (r = 0.47 with Risk Score) — stronger than loan size or account balance.
"Monitor" customers are as valuable as "Grow" customers (~$8.2K avg. balance) but carry more than double the credit utilization (73.8% vs. 32.9%).
50% of High Value customers are dormant (180+ days since last transaction) — a clear reactivation opportunity.
Value × Risk Segments
	Risk: Low	Risk: High
Value: High	🟢 Grow (7.0%)	🟠 Monitor (13.2%)
Value: Low/Medium	🔵 Develop (68.4%)	🔴 Review (11.3%)

Full findings, evidence, and five business recommendations are documented in docs/business_insights.md.

▶️ How to Run
bash
# 1. Install dependencies
pip install pandas matplotlib

# 2. Run the Python pipeline in order
python python/data_inspection.py
python python/data_quality_check.py
python python/data_cleaning.py
python python/feature_engineering.py
python python/eda.py

# 3. Run the SQL scripts (sql/01 → 06) against banking_features
#    in your preferred SQL engine (e.g., SQL Server, PostgreSQL)

Each Python script writes a text report to python/report/, and eda.py saves 8 charts to outputs/eda/.

📄 Deliverables
docs/business_understanding.md — problem framing and scope
docs/data_dictionary.md — field-level documentation
docs/business_insights.md — findings, Value × Risk analysis, and recommendations
Full Project Report (Word) — executive summary through appendix, formatted for stakeholders
⚠️ Limitations
Anomaly is a pre-existing flag, not confirmed fraud/default — treated as one signal among several.
Correlation ≠ causation; relationships describe association only.
Value/risk thresholds are analytical business rules, not regulatory or empirically calibrated cutoffs.
The dataset is a snapshot (most recent record per domain), not full customer history.
Recommendations require validation against real outcomes before operational use.
👤 Author

Data Analyst case study — built with SQL and Python as a portfolio project demonstrating an end-to-end analytics workflow: data cleaning → feature engineering → EDA → segmentation → business recommendations.

