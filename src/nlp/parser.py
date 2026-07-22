import pandas as pd
import re

# Sample analysis data
data = {
    "company_id": [1, 2, 3, 4],
    "metric_type": [
        "Revenue CAGR",
        "Profit CAGR",
        "ROE",
        "Sales Growth"
    ],
    "analysis_text": [
        "10 Years: 21%",
        "5 Years: 15%",
        "3 Years: 12%",
        "Invalid Text"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

parsed_results = []
failed_results = []

# Regex pattern
pattern = r"(\d+)\s*Years?:?\s*([\d.]+)%"

# Parse text
for _, row in df.iterrows():
    match = re.search(pattern, row["analysis_text"])

    if match:
        parsed_results.append({
            "company_id": row["company_id"],
            "metric_type": row["metric_type"],
            "period_years": int(match.group(1)),
            "value_pct": float(match.group(2))
        })
    else:
        failed_results.append(row)

# Convert to DataFrames
parsed_df = pd.DataFrame(parsed_results)
failed_df = pd.DataFrame(failed_results)

# Save output files
parsed_df.to_csv("output/analysis_parsed.csv", index=False)
failed_df.to_csv("output/parse_failures.csv", index=False)

# Print results
print("\n===== Parsed Data =====")
print(parsed_df)

print("\n===== Failed Records =====")
print(failed_df)

print("\nDay 29 Completed Successfully!")
print("Files Saved:")
print("1. output/analysis_parsed.csv")
print("2. output/parse_failures.csv")