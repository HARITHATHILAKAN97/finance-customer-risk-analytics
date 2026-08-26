# ============================================================
# FINANCE CUSTOMER RISK & PROFITABILITY ANALYTICS
# 01 - DATA INSPECTION
# ============================================================

import pandas as pd
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

# Find the main project folder
base_path = Path(__file__).resolve().parents[1]

# Raw dataset location
file_path = (
    base_path
    / "data"
    / "raw"
    / "Comprehensive_Banking_Database.csv"
)

# Report folder inside python/
report_folder = base_path / "python" / "report"

# Create report folder if it doesn't exist
report_folder.mkdir(parents=True, exist_ok=True)

# Report file
report_file = report_folder / "data_inspection_report.txt"


# ============================================================
# 2. LOAD DATA
# ============================================================

df = pd.read_csv(file_path)


# ============================================================
# 3. CREATE REPORT
# ============================================================

# We will store all inspection results in this list
report = []


# ============================================================
# 4. BASIC DATASET INFORMATION
# ============================================================

report.append("=" * 70)
report.append("FINANCE CUSTOMER RISK & PROFITABILITY ANALYTICS")
report.append("DATA INSPECTION REPORT")
report.append("=" * 70)

report.append("\n1. BASIC DATASET INFORMATION")
report.append("-" * 50)

report.append(f"Dataset file: {file_path.name}")
report.append(f"Number of rows: {df.shape[0]}")
report.append(f"Number of columns: {df.shape[1]}")


# ============================================================
# 5. FIRST 5 ROWS
# ============================================================

report.append("\n2. FIRST 5 ROWS")
report.append("-" * 50)

report.append(df.head().to_string())


# ============================================================
# 6. COLUMN NAMES
# ============================================================

report.append("\n3. COLUMN NAMES")
report.append("-" * 50)

for column in df.columns:
    report.append(column)


# ============================================================
# 7. DATA TYPES
# ============================================================

report.append("\n4. DATA TYPES")
report.append("-" * 50)

report.append(df.dtypes.to_string())


# ============================================================
# 8. MISSING VALUES
# ============================================================

report.append("\n5. MISSING VALUE CHECK")
report.append("-" * 50)

missing_values = df.isnull().sum()

report.append(missing_values.to_string())

report.append(
    f"\nTotal missing values: {missing_values.sum()}"
)


# ============================================================
# 9. DUPLICATE ROWS
# ============================================================

report.append("\n6. DUPLICATE ROW CHECK")
report.append("-" * 50)

duplicate_rows = df.duplicated().sum()

report.append(
    f"Duplicate rows: {duplicate_rows}"
)


# ============================================================
# 10. CUSTOMER ID CHECK
# ============================================================

report.append("\n7. CUSTOMER ID CHECK")
report.append("-" * 50)

unique_customers = df["Customer ID"].nunique()
duplicate_customers = df["Customer ID"].duplicated().sum()

report.append(
    f"Total rows: {len(df)}"
)

report.append(
    f"Unique Customer IDs: {unique_customers}"
)

report.append(
    f"Duplicate Customer IDs: {duplicate_customers}"
)


# ============================================================
# 11. OTHER ID CHECKS
# ============================================================

report.append("\n8. IDENTIFIER CHECK")
report.append("-" * 50)

id_columns = [
    "Customer ID",
    "TransactionID",
    "Loan ID",
    "CardID",
    "Feedback ID"
]

for column in id_columns:

    unique_count = df[column].nunique()
    duplicate_count = df[column].duplicated().sum()

    report.append(
        f"{column} → "
        f"Unique: {unique_count} | "
        f"Duplicates: {duplicate_count}"
    )


# ============================================================
# 12. NUMERICAL SUMMARY
# ============================================================

report.append("\n9. NUMERICAL SUMMARY")
report.append("-" * 50)

report.append(
    df.describe().to_string()
)


# ============================================================
# 13. CATEGORICAL VARIABLES
# ============================================================

report.append("\n10. CATEGORICAL VALUE COUNTS")
report.append("-" * 50)


categorical_columns = [
    "Gender",
    "Account Type",
    "Transaction Type",
    "Loan Type",
    "Loan Status",
    "Card Type",
    "Feedback Type",
    "Resolution Status",
    "Anomaly"
]

for column in categorical_columns:

    report.append(f"\n{column}:")

    report.append(
        df[column].value_counts().to_string()
    )


# ============================================================
# 14. NUMERICAL RANGE CHECKS
# ============================================================

report.append("\n11. NUMERICAL RANGE CHECKS")
report.append("-" * 50)


numeric_columns = [
    "Age",
    "Account Balance",
    "Transaction Amount",
    "Loan Amount",
    "Interest Rate",
    "Credit Limit",
    "Credit Card Balance",
    "Minimum Payment Due",
    "Rewards Points"
]

for column in numeric_columns:

    minimum = df[column].min()
    maximum = df[column].max()

    report.append(
        f"{column} → "
        f"Minimum: {minimum} | "
        f"Maximum: {maximum}"
    )


# ============================================================
# 15. FINANCIAL LOGIC CHECKS
# ============================================================

report.append("\n12. FINANCIAL LOGIC CHECKS")
report.append("-" * 50)


# Negative account balance
negative_account_balance = (
    df["Account Balance"] < 0
).sum()

report.append(
    f"Negative Account Balances: "
    f"{negative_account_balance}"
)


# Negative transaction amount
negative_transaction = (
    df["Transaction Amount"] < 0
).sum()

report.append(
    f"Negative Transaction Amounts: "
    f"{negative_transaction}"
)


# Negative loan amount
negative_loan = (
    df["Loan Amount"] < 0
).sum()

report.append(
    f"Negative Loan Amounts: "
    f"{negative_loan}"
)


# Credit card balance above credit limit
balance_above_limit = (
    df["Credit Card Balance"]
    > df["Credit Limit"]
).sum()

report.append(
    f"Credit Card Balance > Credit Limit: "
    f"{balance_above_limit}"
)


# ============================================================
# 16. LOAN TERM CHECK
# ============================================================

report.append("\n13. LOAN TERM CHECK")
report.append("-" * 50)

loan_terms = sorted(
    df["Loan Term"].unique()
)

report.append(
    f"Loan Term values: {loan_terms}"
)


# ============================================================
# 17. DATE COLUMN CHECK
# ============================================================

report.append("\n14. DATE COLUMN CHECK")
report.append("-" * 50)


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

    report.append(
        f"{column} → "
        f"Data type: {df[column].dtype}"
    )


# ============================================================
# 18. DATE VALIDATION
# ============================================================

report.append("\n15. DATE VALIDATION")
report.append("-" * 50)


for column in date_columns:

    converted_dates = pd.to_datetime(
        df[column],
        errors="coerce"
    )

    invalid_dates = converted_dates.isnull().sum()

    report.append(
        f"{column} → "
        f"Invalid dates: {invalid_dates}"
    )


# ============================================================
# 19. ANOMALY CHECK
# ============================================================

report.append("\n16. ANOMALY CHECK")
report.append("-" * 50)


anomaly_counts = df["Anomaly"].value_counts()

report.append(
    anomaly_counts.to_string()
)

report.append("\nAnomaly percentages:")

anomaly_percentage = (
    df["Anomaly"]
    .value_counts(normalize=True)
    * 100
)

report.append(
    anomaly_percentage.to_string()
)


# ============================================================
# 20. CREDIT UTILIZATION PREVIEW
# ============================================================

report.append("\n17. CREDIT UTILIZATION PREVIEW")
report.append("-" * 50)


credit_utilization = (
    df["Credit Card Balance"]
    / df["Credit Limit"]
) * 100

report.append(
    credit_utilization.describe().to_string()
)

report.append(
    f"\nCustomers with utilization > 80%: "
    f"{(credit_utilization > 80).sum()}"
)

report.append(
    f"Customers with utilization > 100%: "
    f"{(credit_utilization > 100).sum()}"
)


# ============================================================
# 21. FINAL SUMMARY
# ============================================================

report.append("\n" + "=" * 70)
report.append("FINAL INSPECTION SUMMARY")
report.append("=" * 70)

report.append(
    f"Rows: {df.shape[0]}"
)

report.append(
    f"Columns: {df.shape[1]}"
)

report.append(
    f"Missing values: {df.isnull().sum().sum()}"
)

report.append(
    f"Duplicate rows: {df.duplicated().sum()}"
)

report.append(
    f"Unique customers: {df['Customer ID'].nunique()}"
)

report.append("\nInspection completed successfully.")

report.append(
    "\nNOTE: No data cleaning or modification was performed."
)


# ============================================================
# 22. SAVE REPORT
# ============================================================

with open(
    report_file,
    "w",
    encoding="utf-8"
) as file:

    file.write("\n".join(report))


print("=" * 60)
print("DATA INSPECTION COMPLETED")
print("=" * 60)

print(
    f"\nReport saved to:\n{report_file}"
)