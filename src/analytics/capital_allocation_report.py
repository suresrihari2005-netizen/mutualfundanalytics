import pandas as pd

# Sample capital allocation data
df = pd.DataFrame({
    "Company": [
        "ABC Ltd",
        "XYZ Industries",
        "Growth Corp",
        "Future Tech"
    ],
    "Capital (Crore)": [500, 300, 150, 50]
})

# Calculate allocation percentage
total_capital = df["Capital (Crore)"].sum()

df["Allocation (%)"] = (
    df["Capital (Crore)"] / total_capital * 100
).round(2)

# Save report
df.to_csv("output/capital_allocation_report.csv", index=False)

print("\n===== Capital Allocation Report =====")
print(df)

print("\nDay 32 Completed Successfully!")
print("Saved: output/capital_allocation_report.csv")