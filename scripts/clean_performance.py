import pandas as pd

# Load data
df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Remove duplicates
df = df.drop_duplicates()

# Convert numeric columns
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows with invalid expense ratio
df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

# Standardize text columns
df["risk_grade"] = df["risk_grade"].str.strip().str.upper()
df["category"] = df["category"].str.strip()

# Save cleaned file
df.to_csv(
    "data/proccessed/07_scheme_performance_cleaned.csv",
    index=False
)

print("Scheme Performance cleaned successfully!")
print("Final Shape:", df.shape)