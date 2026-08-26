# ============================================================
# FINANCE CUSTOMER RISK & PROFITABILITY ANALYTICS
# 02 - DATA QUALITY CHECK
# ============================================================

import pandas as pd
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

# Find the main project folder
base_path = Path(__file__).resolve().parents[1]

# Raw dataset
file_path = (
    base_path
    / "data"
    / "raw"
    / "Comprehensive_Banking_Database.csv"
)

# Report folder
report_folder = base_path / "python" / "report"

# Create report folder if it does not exist
report_folder.mkdir(parents=True, exist_ok=True)

# Quality report
report_file = report_folder / "data_quality_report.txt"


# ============================================================
# 2. LOAD DATA
# ============================================================

df = pd.read_csv(file_path)


# ============================================================
# 3. CREATE REPORT
# ============================================================

report = []


report.append("=" * 70)
report.append("FINANCE CUSTOMER RISK & PROFITABILITY ANALYTICS")
report.append("DATA QUALITY CHECK REPORT")
report.append("=" * 70)


# ============================================================
# 4. DATASET STRUCTURE CHECK
# ============================================================

report.append("\n1. DATASET STRUCTURE CHECK")
report.append("-" * 50)

expected_rows = 5000
expected_columns = 40

actual_rows = df.shape[0]
actual_columns = df.shape[1]

report.append(
    f"Expected rows: {expected_rows}"
)

report.append(
    f"Actual rows: {actual_rows}"
)

if actual_rows == expected_rows:
    report.append("Row count check: PASS")
else:
    report.append("Row count check: REVIEW")


report.append(
    f"\nExpected columns: {expected_columns}"
)

report.append(
    f"Actual columns: {actual_columns}"
)

if actual_columns == expected_columns:
    report.append("Column count check: PASS")
else:
    report.append("Column count check: REVIEW")


# ============================================================
# 5. MISSING VALUE CHECK
# ============================================================

report.append("\n2. MISSING VALUE CHECK")
report.append("-" * 50)

missing_values = df.isnull().sum()

total_missing = missing_values.sum()

report.append(
    f"Total missing values: {total_missing}"
)

if total_missing == 0:
    report.append("Missing value check: PASS")
else:
    report.append("Missing value check: REVIEW")

# Show columns with missing values
columns_with_missing = missing_values[
    missing_values > 0
]

if len(columns_with_missing) > 0:

    report.append("\nColumns with missing values:")

    report.append(
        columns_with_missing.to_string()
    )

else:

    report.append(
        "No columns contain missing values."
    )


# ============================================================
# 6. DUPLICATE ROW CHECK
# ============================================================

report.append("\n3. DUPLICATE ROW CHECK")
report.append("-" * 50)

duplicate_rows = df.duplicated().sum()

report.append(
    f"Duplicate rows: {duplicate_rows}"
)

if duplicate_rows == 0:
    report.append("Duplicate row check: PASS")
else:
    report.append("Duplicate row check: REVIEW")


# ============================================================
# 7. CUSTOMER ID QUALITY CHECK
# ============================================================

report.append("\n4. CUSTOMER ID CHECK")
report.append("-" * 50)

unique_customer_ids = df["Customer ID"].nunique()

duplicate_customer_ids = (
    df["Customer ID"].duplicated().sum()
)

report.append(
    f"Total Customer IDs: {len(df)}"
)

report.append(
    f"Unique Customer IDs: {unique_customer_ids}"
)

report.append(
    f"Duplicate Customer IDs: {duplicate_customer_ids}"
)

if (
    unique_customer_ids == len(df)
    and duplicate_customer_ids == 0
):
    report.append("Customer ID check: PASS")
else:
    report.append("Customer ID check: REVIEW")


# ============================================================
# 8. ID NULL CHECK
# ============================================================

report.append("\n5. IDENTIFIER NULL CHECK")
report.append("-" * 50)

id_columns = [
    "Customer ID",
    "TransactionID",
    "Loan ID",
    "CardID",
    "Feedback ID"
]

for column in id_columns:

    null_count = df[column].isnull().sum()

    report.append(
        f"{column}: {null_count} missing"
    )


# ============================================================
# 9. AGE VALIDATION
# ============================================================

report.append("\n6. AGE VALIDATION")
report.append("-" * 50)

invalid_age = (
    (df["Age"] < 18)
    | (df["Age"] > 100)
).sum()

report.append(
    f"Age values below 18 or above 100: {invalid_age}"
)

if invalid_age == 0:
    report.append("Age check: PASS")
else:
    report.append("Age check: REVIEW")


# ============================================================
# 10. FINANCIAL NEGATIVE VALUE CHECK
# ============================================================

report.append("\n7. NEGATIVE FINANCIAL VALUE CHECK")
report.append("-" * 50)

financial_columns = [
    "Account Balance",
    "Transaction Amount",
    "Loan Amount",
    "Credit Limit",
    "Credit Card Balance",
    "Minimum Payment Due",
    "Rewards Points"
]

for column in financial_columns:

    negative_count = (
        df[column] < 0
    ).sum()

    report.append(
        f"{column}: {negative_count} negative values"
    )


# ============================================================
# 11. CREDIT LIMIT CHECK
# ============================================================

report.append("\n8. CREDIT CARD LIMIT CHECK")
report.append("-" * 50)

balance_above_limit = (
    df["Credit Card Balance"]
    > df["Credit Limit"]
).sum()

report.append(
    f"Credit card balance above credit limit: "
    f"{balance_above_limit}"
)

if balance_above_limit == 0:
    report.append("Credit limit check: PASS")
else:
    report.append("Credit limit check: REVIEW")


# ============================================================
# 12. LOAN TERM VALIDATION
# ============================================================

report.append("\n9. LOAN TERM VALIDATION")
report.append("-" * 50)

expected_loan_terms = [
    12,
    24,
    36,
    48,
    60
]

actual_loan_terms = sorted(
    df["Loan Term"].unique()
)

report.append(
    f"Expected loan terms: {expected_loan_terms}"
)

report.append(
    f"Actual loan terms: {actual_loan_terms}"
)

if actual_loan_terms == expected_loan_terms:
    report.append("Loan term check: PASS")
else:
    report.append("Loan term check: REVIEW")


# ============================================================
# 13. CATEGORICAL VALUE VALIDATION
# ============================================================

report.append("\n10. CATEGORICAL VALUE CHECK")
report.append("-" * 50)


expected_categories = {

    "Account Type": [
        "Savings",
        "Current"
    ],

    "Transaction Type": [
        "Deposit",
        "Withdrawal",
        "Transfer"
    ],

    "Loan Type": [
        "Mortgage",
        "Auto",
        "Personal"
    ],

    "Loan Status": [
        "Approved",
        "Rejected",
        "Closed"
    ],

    "Card Type": [
        "AMEX",
        "MasterCard",
        "Visa"
    ],

    "Feedback Type": [
        "Suggestion",
        "Complaint",
        "Praise"
    ],

    "Resolution Status": [
        "Pending",
        "Resolved"
    ],

    "Gender": [
        "Male",
        "Female",
        "Other"
    ],

    "Anomaly": [
        1,
        -1
    ]
}


for column, expected_values in expected_categories.items():

    actual_values = sorted(
        df[column].dropna().unique().tolist()
    )

    expected_values_sorted = sorted(
        expected_values
    )

    report.append(f"\n{column}")

    report.append(
        f"Expected: {expected_values_sorted}"
    )

    report.append(
        f"Actual: {actual_values}"
    )

    if actual_values == expected_values_sorted:

        report.append(
            "Category check: PASS"
        )

    else:

        report.append(
            "Category check: REVIEW"
        )


# ============================================================
# 14. INTEREST RATE VALIDATION
# ============================================================

report.append("\n11. INTEREST RATE VALIDATION")
report.append("-" * 50)

invalid_interest_rate = (
    (df["Interest Rate"] < 0)
    | (df["Interest Rate"] > 100)
).sum()

report.append(
    f"Interest rates below 0% or above 100%: "
    f"{invalid_interest_rate}"
)

if invalid_interest_rate == 0:
    report.append("Interest rate check: PASS")
else:
    report.append("Interest rate check: REVIEW")


# ============================================================
# 15. CREDIT UTILIZATION CHECK
# ============================================================

report.append("\n12. CREDIT UTILIZATION CHECK")
report.append("-" * 50)

credit_utilization = (
    df["Credit Card Balance"]
    / df["Credit Limit"]
) * 100

invalid_utilization = (
    credit_utilization < 0
).sum()

above_100_utilization = (
    credit_utilization > 100
).sum()

report.append(
    f"Negative utilization values: "
    f"{invalid_utilization}"
)

report.append(
    f"Utilization above 100%: "
    f"{above_100_utilization}"
)

if invalid_utilization == 0:
    report.append(
        "Credit utilization calculation: PASS"
    )
else:
    report.append(
        "Credit utilization calculation: REVIEW"
    )


# ============================================================
# 16. DATE QUALITY CHECK
# ============================================================

report.append("\n13. DATE QUALITY CHECK")
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

    converted_dates = pd.to_datetime(
        df[column],
        errors="coerce"
    )

    invalid_dates = converted_dates.isnull().sum()

    report.append(
        f"{column}: "
        f"{invalid_dates} invalid dates"
    )


# ============================================================
# 17. ANOMALY FLAG CHECK
# ============================================================

report.append("\n14. ANOMALY FLAG CHECK")
report.append("-" * 50)

valid_anomaly_values = [-1, 1]

invalid_anomaly_values = df[
    ~df["Anomaly"].isin(valid_anomaly_values)
]["Anomaly"].count()

report.append(
    f"Invalid anomaly values: "
    f"{invalid_anomaly_values}"
)

if invalid_anomaly_values == 0:
    report.append("Anomaly flag check: PASS")
else:
    report.append("Anomaly flag check: REVIEW")


# ============================================================
# 18. DATA QUALITY SUMMARY
# ============================================================

report.append("\n" + "=" * 70)
report.append("DATA QUALITY SUMMARY")
report.append("=" * 70)

report.append(
    "\nThe above checks should be reviewed before data cleaning."
)

report.append(
    "\nImportant principle:"
)

report.append(
    "A REVIEW result does not automatically mean the data is wrong."
)

report.append(
    "It means the value requires investigation before deciding"
    " whether it should be cleaned."
)


# ============================================================
# 19. SAVE REPORT
# ============================================================

with open(
    report_file,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "\n".join(report)
    )


# ============================================================
# 20. COMPLETION MESSAGE
# ============================================================

print("=" * 60)
print("DATA QUALITY CHECK COMPLETED")
print("=" * 60)

print(
    f"\nQuality report saved to:\n{report_file}"
)