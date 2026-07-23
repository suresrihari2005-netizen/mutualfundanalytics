import pandas as pd

# Sample clustered company data
df = pd.DataFrame({
    "company_id": [1, 2, 3, 4, 5],
    "cluster_id": [0, 1, 0, 2, 1],
    "roe": [18, 24, 15, 10, 30],
    "debt_equity": [0.4, 0.2, 0.8, 1.5, 0.3],
    "revenue_growth": [12, 18, 10, 5, 22],
    "fcf_growth": [15, 20, 11, 4, 25],
    "opm": [22, 30, 18, 12, 35]
})

# Cluster names
cluster_names = {
    0: "Quality",
    1: "Growth",
    2: "Value",
    3: "Turnaround",
    4: "Dividend"
}

df["cluster_name"] = df["cluster_id"].map(cluster_names)

# Portfolio statistics
portfolio_stats = (
    df.groupby(["cluster_id", "cluster_name"])
      .mean(numeric_only=True)
      .reset_index()
)

print("\n===== Portfolio Statistics =====")
print(portfolio_stats)

# Save portfolio statistics
portfolio_stats.to_csv(
    "output/portfolio_stats.csv",
    index=False
)

# Outlier detection using Z-score
numeric_cols = [
    "roe",
    "debt_equity",
    "revenue_growth",
    "fcf_growth",
    "opm"
]

outliers = []

for col in numeric_cols:

    mean = df[col].mean()
    std = df[col].std()

    if std == 0:
        continue

    for _, row in df.iterrows():

        z_score = (row[col] - mean) / std

        if abs(z_score) > 1.5:

            outliers.append({
                "company_id": row["company_id"],
                "metric": col,
                "value": row[col],
                "z_score": round(z_score, 2)
            })

# Create outlier report
outlier_df = pd.DataFrame(outliers)

print("\n===== Outlier Report =====")
print(outlier_df)

# Save outlier report
outlier_df.to_csv(
    "output/outlier_report.csv",
    index=False
)

print("\nDay 37 Completed Successfully!")
print("Saved:")
print("1. output/portfolio_stats.csv")
print("2. output/outlier_report.csv")