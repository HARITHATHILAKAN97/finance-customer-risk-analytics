# ============================================================
# FINANCE CUSTOMER RISK & PROFITABILITY ANALYTICS
# 04 - FEATURE ENGINEERING
# ============================================================

import pandas as pd
from pathlib import Path


# ============================================================
# 1. PROJECT PATH
# ============================================================

base_path = Path(__file__).resolve().parents[1]

input_file = (
    base_path
    / "data"
    / "cleaned"
    / "banking_cleaned.csv"
)

output_folder = (
    base_path
    / "data"
    / "processed"
)

report_folder = (
    base_path
    / "python"
    / "report"
)

output_folder.mkdir(
    parents=True,
    exist_ok=True
)

report_folder.mkdir(
    parents=True,
    exist_ok=True
)

output_file = (
    output_folder
    / "banking_features.csv"
)

report_file = (
    report_folder
    / "feature_engineering_report.txt"
)


# ============================================================
# 2. LOAD CLEANED DATA
# ============================================================

df = pd.read_csv(input_file)

print("Data loaded successfully.")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ============================================================
# 3. CONVERT DATE COLUMNS
# ============================================================

date_columns = [
    "Date Of Account Opening",
    "Last Transaction Date",
    "Transaction Date",
    "Approval/Rejection Date",
    "Payment Due Date",
    "Last Credit Card Payment Date",
    "Feedback Date",
    "Resolution Date"
]

for column in date_columns:
    df[column] = pd.to_datetime(
        df[column],
        errors="coerce"
    )

print("\nDate columns converted.")


# ============================================================
# 4. AGE GROUP
# ============================================================

df["Age Group"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 65, 100],
    labels=[
        "18-25",
        "26-35",
        "36-45",
        "46-55",
        "56-65",
        "66+"
    ]
)

print("Age Group created.")


# ============================================================
# 5. ACCOUNT AGE
# ============================================================

latest_date = df["Transaction Date"].max()

df["Account Age Years"] = (
    latest_date
    - df["Date Of Account Opening"]
).dt.days / 365.25

df["Account Age Years"] = (
    df["Account Age Years"].round(1)
)

print("Account Age Years created.")


# ============================================================
# 6. TRANSACTION RECENCY
# ============================================================

df["Transaction Recency Days"] = (
    latest_date
    - df["Last Transaction Date"]
).dt.days

print("Transaction Recency Days created.")


# ============================================================
# 7. CREDIT UTILIZATION
# ============================================================

df["Credit Utilization %"] = (
    df["Credit Card Balance"]
    / df["Credit Limit"]
) * 100

df["Credit Utilization %"] = (
    df["Credit Utilization %"].round(2)
)

print("Credit Utilization % created.")


# ============================================================
# 8. AVAILABLE CREDIT
# ============================================================

df["Available Credit"] = (
    df["Credit Limit"]
    - df["Credit Card Balance"]
)

print("Available Credit created.")


# ============================================================
# 9. LOAN TO BALANCE RATIO
# ============================================================

df["Loan to Balance Ratio"] = (
    df["Loan Amount"]
    / df["Account Balance"]
)

df["Loan to Balance Ratio"] = (
    df["Loan to Balance Ratio"].round(2)
)

print("Loan to Balance Ratio created.")


# ============================================================
# 10. PAYMENT TIMING
# ============================================================

df["Payment Timing Days"] = (
    df["Last Credit Card Payment Date"]
    - df["Payment Due Date"]
).dt.days

print("Payment Timing Days created.")


# ============================================================
# 11. COMPLAINT FLAG
# ============================================================

df["Complaint Flag"] = (
    df["Feedback Type"] == "Complaint"
).astype(int)

print("Complaint Flag created.")


# ============================================================
# 12. PENDING FEEDBACK FLAG
# ============================================================

df["Pending Feedback Flag"] = (
    df["Resolution Status"] == "Pending"
).astype(int)

print("Pending Feedback Flag created.")


# ============================================================
# 13. ANOMALY FLAG
# ============================================================

df["Anomaly Flag"] = (
    df["Anomaly"] == -1
).astype(int)

print("Anomaly Flag created.")


# ============================================================
# 14. SIMPLE BUSINESS RISK SCORE
# ============================================================

df["Risk Score"] = 0


# High credit utilization
df.loc[
    df["Credit Utilization %"] > 75,
    "Risk Score"
] += 2


# Payment after due date
df.loc[
    df["Payment Timing Days"] > 0,
    "Risk Score"
] += 2


# Large loan
df.loc[
    df["Loan Amount"] > 40000,
    "Risk Score"
] += 1


# Customer has a pending complaint
df.loc[
    (df["Complaint Flag"] == 1)
    & (df["Pending Feedback Flag"] == 1),
    "Risk Score"
] += 1


print("Risk Score created.")


# ============================================================
# 15. RISK LEVEL
# ============================================================

df["Risk Level"] = "Low"

df.loc[
    df["Risk Score"].between(2, 3),
    "Risk Level"
] = "Medium"

df.loc[
    df["Risk Score"] >= 4,
    "Risk Level"
] = "High"

print("Risk Level created.")


# ============================================================
# 16. CUSTOMER VALUE SCORE
# ============================================================

# Convert three financial indicators
# into scores from 0 to 100.

balance_score = (
    df["Account Balance"]
    / df["Account Balance"].max()
) * 100

loan_score = (
    df["Loan Amount"]
    / df["Loan Amount"].max()
) * 100

reward_score = (
    df["Rewards Points"]
    / df["Rewards Points"].max()
) * 100


df["Customer Value Score"] = (
    balance_score * 0.50
    + loan_score * 0.30
    + reward_score * 0.20
)

df["Customer Value Score"] = (
    df["Customer Value Score"].round(2)
)

print("Customer Value Score created.")


# ============================================================
# 17. CUSTOMER VALUE SEGMENT
# ============================================================

df["Customer Value Segment"] = "Low Value"

df.loc[
    df["Customer Value Score"].between(33, 66),
    "Customer Value Segment"
] = "Medium Value"

df.loc[
    df["Customer Value Score"] > 66,
    "Customer Value Segment"
] = "High Value"

print("Customer Value Segment created.")


# ============================================================
# 18. VALUE × RISK SEGMENT
# ============================================================

df["Value Risk Segment"] = "Develop"

df.loc[
    (df["Customer Value Segment"] == "High Value")
    & (df["Risk Level"] == "Low"),
    "Value Risk Segment"
] = "Grow"

df.loc[
    (df["Customer Value Segment"] == "High Value")
    & (df["Risk Level"] != "Low"),
    "Value Risk Segment"
] = "Monitor"

df.loc[
    (df["Customer Value Segment"] != "High Value")
    & (df["Risk Level"] == "High"),
    "Value Risk Segment"
] = "Review"

print("Value × Risk Segment created.")


# ============================================================
# 19. ROUND NUMERIC FEATURES
# ============================================================

df["Account Age Years"] = (
    df["Account Age Years"].round(1)
)

df["Loan to Balance Ratio"] = (
    df["Loan to Balance Ratio"].round(2)
)

df["Credit Utilization %"] = (
    df["Credit Utilization %"].round(2)
)


# ============================================================
# 20. SAVE FEATURE-ENGINEERED DATA
# ============================================================

df.to_csv(
    output_file,
    index=False
)

print("\nFeature-engineered dataset saved.")


# ============================================================
# 21. CREATE REPORT
# ============================================================

new_columns = [
    "Age Group",
    "Account Age Years",
    "Transaction Recency Days",
    "Credit Utilization %",
    "Available Credit",
    "Loan to Balance Ratio",
    "Payment Timing Days",
    "Complaint Flag",
    "Pending Feedback Flag",
    "Anomaly Flag",
    "Risk Score",
    "Risk Level",
    "Customer Value Score",
    "Customer Value Segment",
    "Value Risk Segment"
]

report = []

report.append("FEATURE ENGINEERING REPORT")
report.append("=" * 50)

report.append(
    f"Rows: {df.shape[0]}"
)

report.append(
    f"Columns after feature engineering: {df.shape[1]}"
)

report.append("\nNew columns created:")

for column in new_columns:
    report.append("- " + column)

report.append("\nOutput file:")
report.append(str(output_file))


# Save report

with open(
    report_file,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "\n".join(report)
    )


print("Feature engineering report saved.")
print("\nFEATURE ENGINEERING COMPLETED!")