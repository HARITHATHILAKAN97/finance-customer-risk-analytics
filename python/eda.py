# ============================================================
# FINANCE CUSTOMER RISK & PROFITABILITY ANALYTICS
# 05 - EXPLORATORY DATA ANALYSIS
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================================
# 1. PROJECT PATH
# ============================================================

base_path = Path(__file__).resolve().parents[1]

input_file = (
    base_path
    / "data"
    / "processed"
    / "banking_features.csv"
)

output_folder = (
    base_path
    / "outputs"
    / "eda"
)

report_folder = (
    base_path
    / "python"
    / "report"
)

# Create folders if they don't exist

output_folder.mkdir(
    parents=True,
    exist_ok=True
)

report_folder.mkdir(
    parents=True,
    exist_ok=True
)

report_file = (
    report_folder
    / "eda_report.txt"
)


# ============================================================
# 2. LOAD DATA
# ============================================================

df = pd.read_csv(input_file)

print("Data loaded successfully.")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ============================================================
# 3. BASIC DATA SUMMARY
# ============================================================

print("\n========== BASIC SUMMARY ==========")

print("\nDataset Shape:")
print(df.shape)

print("\nNumeric Summary:")
print(df.describe())


# ============================================================
# 4. CUSTOMER DEMOGRAPHICS
# ============================================================

print("\n========== CUSTOMER DEMOGRAPHICS ==========")

print("\nGender Distribution:")
print(df["Gender"].value_counts())

print("\nAge Group Distribution:")
print(df["Age Group"].value_counts().sort_index())

print("\nTop 10 Cities:")
print(df["City"].value_counts().head(10))


# ============================================================
# 5. ACCOUNT ANALYSIS
# ============================================================

print("\n========== ACCOUNT ANALYSIS ==========")

print("\nAccount Type:")
print(df["Account Type"].value_counts())

print("\nAverage Account Balance by Account Type:")

print(
    df.groupby("Account Type")["Account Balance"]
    .mean()
    .round(2)
)


# ============================================================
# 6. TRANSACTION ANALYSIS
# ============================================================

print("\n========== TRANSACTION ANALYSIS ==========")

print("\nTransaction Type:")
print(df["Transaction Type"].value_counts())

print("\nTransaction Amount Statistics:")

print(
    df["Transaction Amount"]
    .describe()
    .round(2)
)

print("\nAverage Transaction Amount by Type:")

print(
    df.groupby("Transaction Type")["Transaction Amount"]
    .mean()
    .round(2)
)


# ============================================================
# 7. LOAN ANALYSIS
# ============================================================

print("\n========== LOAN ANALYSIS ==========")

print("\nLoan Type:")
print(df["Loan Type"].value_counts())

print("\nLoan Status:")
print(df["Loan Status"].value_counts())

print("\nAverage Loan Amount by Loan Type:")

print(
    df.groupby("Loan Type")["Loan Amount"]
    .mean()
    .round(2)
)

print("\nAverage Interest Rate by Loan Type:")

print(
    df.groupby("Loan Type")["Interest Rate"]
    .mean()
    .round(2)
)


# ============================================================
# 8. CREDIT CARD ANALYSIS
# ============================================================

print("\n========== CREDIT CARD ANALYSIS ==========")

print("\nCard Type:")
print(df["Card Type"].value_counts())

print("\nAverage Credit Limit:")

print(
    df["Credit Limit"]
    .mean()
    .round(2)
)

print("\nAverage Credit Card Balance:")

print(
    df["Credit Card Balance"]
    .mean()
    .round(2)
)

print("\nAverage Credit Utilization:")

print(
    df["Credit Utilization %"]
    .mean()
    .round(2)
)


# ============================================================
# 9. RISK ANALYSIS
# ============================================================

print("\n========== RISK ANALYSIS ==========")

print("\nRisk Level Distribution:")
print(df["Risk Level"].value_counts())

print("\nRisk Score Distribution:")
print(df["Risk Score"].value_counts().sort_index())

print("\nAnomaly Distribution:")
print(df["Anomaly Flag"].value_counts())


# ============================================================
# 10. RISK BY CUSTOMER VALUE
# ============================================================

print("\n========== VALUE & RISK ANALYSIS ==========")

print("\nCustomer Value Segment:")
print(
    df["Customer Value Segment"]
    .value_counts()
)

print("\nValue × Risk Segment:")
print(
    df["Value Risk Segment"]
    .value_counts()
)


# ============================================================
# 11. AVERAGE FINANCIAL METRICS BY RISK LEVEL
# ============================================================

print("\n========== FINANCIAL METRICS BY RISK ==========")

risk_summary = (
    df.groupby("Risk Level")
    [
        [
            "Account Balance",
            "Loan Amount",
            "Credit Card Balance",
            "Credit Utilization %",
            "Customer Value Score"
        ]
    ]
    .mean()
    .round(2)
)

print(risk_summary)


# ============================================================
# 12. AVERAGE RISK BY VALUE SEGMENT
# ============================================================

print("\n========== VALUE SEGMENT ANALYSIS ==========")

value_summary = (
    df.groupby("Customer Value Segment")
    [
        [
            "Account Balance",
            "Loan Amount",
            "Credit Utilization %",
            "Risk Score"
        ]
    ]
    .mean()
    .round(2)
)

print(value_summary)


# ============================================================
# 13. CORRELATION ANALYSIS
# ============================================================

print("\n========== CORRELATION ANALYSIS ==========")

correlation_columns = [
    "Age",
    "Account Balance",
    "Transaction Amount",
    "Loan Amount",
    "Interest Rate",
    "Credit Limit",
    "Credit Card Balance",
    "Credit Utilization %",
    "Loan to Balance Ratio",
    "Risk Score",
    "Customer Value Score"
]

correlation_matrix = (
    df[correlation_columns]
    .corr()
    .round(2)
)

print(correlation_matrix)


# ============================================================
# 14. VISUALIZATION 1
# ACCOUNT TYPE
# ============================================================

plt.figure(figsize=(7, 5))

df["Account Type"].value_counts().plot(
    kind="bar"
)

plt.title("Customer Distribution by Account Type")
plt.xlabel("Account Type")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    output_folder / "01_account_type.png"
)

plt.show()


# ============================================================
# 15. VISUALIZATION 2
# LOAN STATUS
# ============================================================

plt.figure(figsize=(7, 5))

df["Loan Status"].value_counts().plot(
    kind="bar"
)

plt.title("Loan Status Distribution")
plt.xlabel("Loan Status")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    output_folder / "02_loan_status.png"
)

plt.show()


# ============================================================
# 16. VISUALIZATION 3
# CREDIT UTILIZATION
# ============================================================

plt.figure(figsize=(7, 5))

plt.hist(
    df["Credit Utilization %"],
    bins=30
)

plt.title("Credit Utilization Distribution")
plt.xlabel("Credit Utilization (%)")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    output_folder / "03_credit_utilization.png"
)

plt.show()


# ============================================================
# 17. VISUALIZATION 4
# LOAN AMOUNT
# ============================================================

plt.figure(figsize=(7, 5))

plt.hist(
    df["Loan Amount"],
    bins=30
)

plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    output_folder / "04_loan_amount.png"
)

plt.show()


# ============================================================
# 18. VISUALIZATION 5
# RISK LEVEL
# ============================================================

plt.figure(figsize=(7, 5))

df["Risk Level"].value_counts().plot(
    kind="bar"
)

plt.title("Customer Risk Level")
plt.xlabel("Risk Level")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    output_folder / "05_risk_level.png"
)

plt.show()


# ============================================================
# 19. VISUALIZATION 6
# VALUE × RISK SEGMENT
# ============================================================

plt.figure(figsize=(8, 5))

df["Value Risk Segment"].value_counts().plot(
    kind="bar"
)

plt.title("Customer Value × Risk Segments")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    output_folder / "06_value_risk_segment.png"
)

plt.show()


# ============================================================
# 20. VISUALIZATION 7
# ACCOUNT BALANCE VS LOAN AMOUNT
# ============================================================

plt.figure(figsize=(7, 5))

plt.scatter(
    df["Account Balance"],
    df["Loan Amount"],
    alpha=0.5
)

plt.title("Account Balance vs Loan Amount")
plt.xlabel("Account Balance")
plt.ylabel("Loan Amount")

plt.tight_layout()

plt.savefig(
    output_folder / "07_balance_vs_loan.png"
)

plt.show()


# ============================================================
# 21. VISUALIZATION 8
# CREDIT UTILIZATION VS RISK SCORE
# ============================================================

plt.figure(figsize=(7, 5))

plt.scatter(
    df["Credit Utilization %"],
    df["Risk Score"],
    alpha=0.5
)

plt.title(
    "Credit Utilization vs Risk Score"
)

plt.xlabel("Credit Utilization (%)")
plt.ylabel("Risk Score")

plt.tight_layout()

plt.savefig(
    output_folder / "08_utilization_vs_risk.png"
)

plt.show()


# ============================================================
# 22. CREATE EDA REPORT
# ============================================================

report = []

report.append("FINANCE CUSTOMER RISK & PROFITABILITY ANALYTICS")
report.append("EDA REPORT")
report.append("=" * 60)

report.append(
    f"\nDataset rows: {df.shape[0]}"
)

report.append(
    f"Dataset columns: {df.shape[1]}"
)


# Customer information

report.append("\n\nCUSTOMER DEMOGRAPHICS")
report.append("-" * 40)

report.append(
    "\nGender Distribution:"
)

report.append(
    df["Gender"]
    .value_counts()
    .to_string()
)

report.append(
    "\nAge Group Distribution:"
)

report.append(
    df["Age Group"]
    .value_counts()
    .sort_index()
    .to_string()
)


# Account

report.append("\n\nACCOUNT ANALYSIS")
report.append("-" * 40)

report.append(
    "\nAccount Type:"
)

report.append(
    df["Account Type"]
    .value_counts()
    .to_string()
)

report.append(
    "\nAverage Account Balance:"
)

report.append(
    df["Account Balance"]
    .mean()
    .round(2)
    .astype(str)
)


# Loan

report.append("\n\nLOAN ANALYSIS")
report.append("-" * 40)

report.append(
    "\nLoan Status:"
)

report.append(
    df["Loan Status"]
    .value_counts()
    .to_string()
)

report.append(
    "\nAverage Loan Amount:"
)

report.append(
    df["Loan Amount"]
    .mean()
    .round(2)
    .astype(str)
)


# Credit

report.append("\n\nCREDIT CARD ANALYSIS")
report.append("-" * 40)

report.append(
    "\nAverage Credit Utilization:"
)

report.append(
    df["Credit Utilization %"]
    .mean()
    .round(2)
    .astype(str)
)


# Risk

report.append("\n\nRISK ANALYSIS")
report.append("-" * 40)

report.append(
    "\nRisk Level Distribution:"
)

report.append(
    df["Risk Level"]
    .value_counts()
    .to_string()
)

report.append(
    "\nAverage Risk Score:"
)

report.append(
    df["Risk Score"]
    .mean()
    .round(2)
    .astype(str)
)


# Value

report.append("\n\nCUSTOMER VALUE ANALYSIS")
report.append("-" * 40)

report.append(
    "\nCustomer Value Segment:"
)

report.append(
    df["Customer Value Segment"]
    .value_counts()
    .to_string()
)


# Value × Risk

report.append("\n\nVALUE × RISK ANALYSIS")
report.append("-" * 40)

report.append(
    df["Value Risk Segment"]
    .value_counts()
    .to_string()
)


# Correlation

report.append("\n\nCORRELATION MATRIX")
report.append("-" * 40)

report.append(
    correlation_matrix.to_string()
)


# ============================================================
# 23. SAVE REPORT
# ============================================================

with open(
    report_file,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "\n".join(report)
    )


print("\nEDA report saved successfully.")

print("\n====================================")
print("EDA COMPLETED SUCCESSFULLY!")
print("====================================")