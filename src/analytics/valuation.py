import pandas as pd

# Sample data
funds = pd.DataFrame({
    "Fund": [
        "SBI Bluechip",
        "Axis Growth",
        "HDFC Equity",
        "ICICI Value",
        "Parag Parikh"
    ],
    "PE Ratio": [22, 28, 18, 15, 30],
    "PB Ratio": [3.2, 4.1, 2.8, 2.1, 5.0]
})

def valuation_label(pe):
    if pe < 18:
        return "Undervalued"
    elif pe <= 25:
        return "Fair Value"
    else:
        return "Overvalued"

funds["Valuation"] = funds["PE Ratio"].apply(valuation_label)

print("\nValuation Summary\n")
print(funds)

funds.to_csv("outputs/valuation_summary.csv", index=False)

print("\nSaved: outputs/valuation_summary.csv")