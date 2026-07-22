import pandas as pd

# Sample company data
df = pd.DataFrame({
    "company": [
        "ABC Ltd",
        "XYZ Industries",
        "Growth Corp",
        "Future Tech"
    ],
    "analysis": [
        "Strong profit growth and low debt",
        "High debt and declining sales",
        "Consistent revenue growth with healthy cash flow",
        "Weak earnings but improving margins"
    ]
})

positive_keywords = [
    "strong",
    "growth",
    "healthy",
    "improving",
    "consistent"
]

negative_keywords = [
    "high debt",
    "declining",
    "weak"
]

def find_pros(text):
    text = text.lower()
    return ", ".join([k for k in positive_keywords if k in text])

def find_cons(text):
    text = text.lower()
    return ", ".join([k for k in negative_keywords if k in text])

df["Pros"] = df["analysis"].apply(find_pros)
df["Cons"] = df["analysis"].apply(find_cons)

df.to_csv("output/pros_cons_generated.csv", index=False)

print("\n===== Pros & Cons Summary =====")
print(df)

print("\nDay 30 Completed Successfully!")
print("Saved: output/pros_cons_generated.csv")