import pandas as pd

# Sample cash flow data
df = pd.DataFrame({
    "Company": [
        "ABC Ltd",
        "XYZ Industries",
        "Growth Corp",
        "Future Tech"
    ],
    "Operating Cash Flow": [1200, 450, -150, 800],
    "Free Cash Flow": [900, 200, -300, 650]
})

def classify_cashflow(fcf):
    if fcf >= 700:
        return "Strong"
    elif fcf >= 0:
        return "Average"
    else:
        return "Weak"

df["Cash Flow Status"] = df["Free Cash Flow"].apply(classify_cashflow)

# Save results
df.to_csv("output/cashflow_intelligence.csv", index=False)

print("\n===== Cash Flow Intelligence =====")
print(df)

print("\nDay 31 Completed Successfully!")
print("Saved: output/cashflow_intelligence.csv")