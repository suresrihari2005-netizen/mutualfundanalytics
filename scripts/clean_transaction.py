import pandas as pd

# Load data
df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert date column
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction type
df["transaction_type"] = df["transaction_type"].str.strip().str.upper()

# Standardize KYC status
df["kyc_status"] = df["kyc_status"].str.strip().str.upper()

# Keep only valid amounts
df = df[df["amount_inr"] > 0]

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/proccessed/08_investor_transactions_cleaned.csv",
    index=False
)

print("Transactions cleaned successfully!")
print("Final Shape:", df.shape)

print("\nTransaction Types:")
print(df["transaction_type"].unique())

print("\nKYC Status:")
print(df["kyc_status"].unique())