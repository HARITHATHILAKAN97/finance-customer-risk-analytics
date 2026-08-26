# ============================================================
# FINANCE CUSTOMER RISK & PROFITABILITY ANALYTICS
# 03 - DATA CLEANING
# ============================================================

import pandas as pd
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

# Main project folder
base_path = Path(__file__).resolve().parents[1]

# Raw dataset
input_file = (
    base_path
    / "data"
    / "raw"
    / "Comprehensive_Banking_Database.csv"
)

# Cleaned data folder
cleaned_folder = (
    base_path
    / "data"
    / "cleaned"
)

# Report folder
report_folder = (
    base_path
    / "python"
    / "report"
)

# Create folders if they don't exist
cleaned_folder.mkdir(
    parents=True,
    exist_ok=True
)

report_folder.mkdir(
    parents=True,
    exist_ok=True
)

# Output files
cleaned_file = (
    cleaned_folder
    / "banking_cleaned.csv"
)

report_file = (
    report_folder
    / "data_cleaning_report.txt"
)


# ============================================================
# 2. LOAD RAW DATA
# ============================================================

df = pd.read_csv(input_file)

# Keep original row count for comparison
original_rows = len(df)


# ============================================================
# 3. CREATE CLEANING REPORT
# ============================================================

report = []

report.append("=" * 70)
report.append("FINANCE CUSTOMER RISK & PROFITABILITY ANALYTICS")
report.append("DATA CLEANING REPORT")
report.append("=" * 70)


# ============================================================
# 4. INITIAL DATASET INFORMATION
# ============================================================

report.append("\n1. INITIAL DATASET")
report.append("-" * 50)

report.append(
    f"Rows before cleaning: {df.shape[0]}"
)

report.append(
    f"Columns before cleaning: {df.shape[1]}"
)


# ============================================================
# 5. REMOVE EXACT DUPLICATE ROWS
# ============================================================

report.append("\n2. DUPLICATE ROW CLEANING")
report.append("-" * 50)

duplicates_before = df.duplicated().sum()

report.append(
    f"Duplicate rows found: {duplicates_before}"
)

if duplicates_before > 0:

    df = df.drop_duplicates()

    report.append(
        f"Duplicate rows removed: {duplicates_before}"
    )

else:

    report.append(
        "No duplicate rows removed."
    )


# ============================================================
# 6. CHECK CUSTOMER ID DUPLICATES
# ============================================================

report.append("\n3. CUSTOMER ID CHECK")
report.append("-" * 50)

customer_duplicates = (
    df["Customer ID"].duplicated().sum()
)

report.append(
    f"Duplicate Customer IDs: {customer_duplicates}"
)

# We do NOT remove these automatically.
# One row = one customer is a business assumption,
# so unexpected duplicate IDs should be investigated.


if customer_duplicates == 0:

    report.append(
        "Customer ID uniqueness confirmed."
    )

else:

    report.append(
        "Customer ID duplicates require investigation."
    )


# ============================================================
# 7. HANDLE MISSING VALUES
# ============================================================

report.append("\n4. MISSING VALUE CLEANING")
report.append("-" * 50)

missing_before = df.isnull().sum().sum()

report.append(
    f"Missing values before cleaning: {missing_before}"
)

if missing_before == 0:

    report.append(
        "No missing values found. No action required."
    )

else:

    report.append(
        "Missing values found. Applying appropriate handling."
    )

    # Numeric columns → median
    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    for column in numeric_columns:

        if df[column].isnull().sum() > 0:

            median_value = df[column].median()

            df[column] = df[column].fillna(
                median_value
            )

            report.append(
                f"{column}: missing values filled with median."
            )

    # Categorical columns → mode
    categorical_columns = df.select_dtypes(
        include="object"
    ).columns

    for column in categorical_columns:

        if df[column].isnull().sum() > 0:

            mode_value = df[column].mode()[0]

            df[column] = df[column].fillna(
                mode_value
            )

            report.append(
                f"{column}: missing values filled with mode."
            )


# ============================================================
# 8. STANDARDIZE TEXT COLUMNS
# ============================================================

report.append("\n5. TEXT STANDARDIZATION")
report.append("-" * 50)

text_columns = [
    "Gender",
    "City",
    "Account Type",
    "Transaction Type",
    "Loan Type",
    "Loan Status",
    "Card Type",
    "Feedback Type",
    "Resolution Status"
]

for column in text_columns:

    if column in df.columns:

        df[column] = (
            df[column]
            .astype(str)
            .str.strip()
        )

        report.append(
            f"{column}: whitespace removed."
        )


# ============================================================
# 9. CONVERT DATE COLUMNS
# ============================================================

report.append("\n6. DATE CONVERSION")
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

    if column in df.columns:

        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )

        report.append(
            f"{column}: converted to datetime."
        )


# ============================================================
# 10. NUMERIC COLUMN CONVERSION
# ============================================================

report.append("\n7. NUMERIC COLUMN CHECK")
report.append("-" * 50)

numeric_columns = [
    "Age",
    "Account Balance",
    "Transaction Amount",
    "Account Balance After Transaction",
    "Loan Amount",
    "Interest Rate",
    "Loan Term",
    "Credit Limit",
    "Credit Card Balance",
    "Minimum Payment Due",
    "Rewards Points",
    "Anomaly"
]

for column in numeric_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

        report.append(
            f"{column}: converted to numeric."
        )


# ============================================================
# 11. CHECK INVALID AGE VALUES
# ============================================================

report.append("\n8. AGE VALIDATION")
report.append("-" * 50)

invalid_age = (
    (df["Age"] < 18)
    | (df["Age"] > 100)
)

invalid_age_count = invalid_age.sum()

report.append(
    f"Invalid age records: {invalid_age_count}"
)

# We do NOT replace ages automatically.
# Invalid values need investigation.

if invalid_age_count == 0:

    report.append(
        "Age values are within the expected range."
    )

else:

    report.append(
        "Invalid ages retained for investigation."
    )


# ============================================================
# 12. CHECK NEGATIVE FINANCIAL VALUES
# ============================================================

report.append("\n9. FINANCIAL VALUE CHECK")
report.append("-" * 50)

financial_columns = [
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
        f"{column}: {negative_count} negative values."
    )


# ============================================================
# 13. CREDIT UTILIZATION CHECK
# ============================================================

report.append("\n10. CREDIT UTILIZATION CHECK")
report.append("-" * 50)

df["Credit Utilization %"] = (
    df["Credit Card Balance"]
    / df["Credit Limit"]
) * 100

report.append(
    "Credit Utilization % calculated successfully."
)


# ============================================================
# 14. PAYMENT DELAY
# ============================================================

report.append("\n11. PAYMENT DELAY FEATURE")
report.append("-" * 50)

df["Payment Delay Days"] = (
    df["Last Credit Card Payment Date"]
    - df["Payment Due Date"]
).dt.days

report.append(
    "Payment Delay Days calculated."
)

report.append(
    "Negative values indicate payment before the due date."
)

report.append(
    "Positive values indicate payment after the due date."
)


# ============================================================
# 15. ACCOUNT AGE
# ============================================================

report.append("\n12. ACCOUNT AGE FEATURE")
report.append("-" * 50)

latest_date = df["Transaction Date"].max()

df["Account Age Days"] = (
    latest_date
    - df["Date Of Account Opening"]
).dt.days

report.append(
    "Account Age Days calculated."
)


# ============================================================
# 16. LOAN EXPOSURE
# ============================================================

report.append("\n13. LOAN EXPOSURE FEATURE")
report.append("-" * 50)

df["Loan Exposure"] = df["Loan Amount"]

report.append(
    "Loan Exposure calculated from Loan Amount."
)


# ============================================================
# 17. ANOMALY FLAG
# ============================================================

report.append("\n14. ANOMALY FLAG")
report.append("-" * 50)

df["Risk Flag"] = df["Anomaly"].map({
    1: "Normal",
    -1: "Flagged"
})

report.append(
    "Risk Flag created from Anomaly."
)


# ============================================================
# 18. FINAL MISSING VALUE CHECK
# ============================================================

report.append("\n15. FINAL QUALITY CHECK")
report.append("-" * 50)

missing_after = df.isnull().sum().sum()

report.append(
    f"Missing values after cleaning: {missing_after}"
)

report.append(
    f"Rows after cleaning: {df.shape[0]}"
)

report.append(
    f"Columns after cleaning: {df.shape[1]}"
)


# ============================================================
# 19. SAVE CLEANED DATA
# ============================================================

df.to_csv(
    cleaned_file,
    index=False
)

report.append("\n16. OUTPUT")
report.append("-" * 50)

report.append(
    f"Cleaned dataset saved to:"
)

report.append(
    str(cleaned_file)
)


# ============================================================
# 20. SAVE CLEANING REPORT
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
# 21. FINAL MESSAGE
# ============================================================

print("=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)

print(
    f"\nCleaned data:\n{cleaned_file}"
)

print(
    f"\nCleaning report:\n{report_file}"
)