import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fund Screener", layout="wide")

st.title("🔍 Mutual Fund Screener")

funds = pd.DataFrame({
    "Fund": [
        "SBI Bluechip",
        "Axis Growth",
        "HDFC Equity",
        "ICICI Value",
        "Parag Parikh"
    ],
    "Category": [
        "Large Cap",
        "Mid Cap",
        "Large Cap",
        "Value",
        "Flexi Cap"
    ],
    "Return (%)": [
        18.4,
        15.2,
        16.9,
        14.8,
        21.3
    ],
    "Expense Ratio": [
        1.20,
        1.05,
        1.10,
        0.95,
        0.85
    ]
})

st.sidebar.header("Filters")

min_return = st.sidebar.slider(
    "Minimum Return (%)",
    0,
    30,
    10
)

max_expense = st.sidebar.slider(
    "Maximum Expense Ratio",
    0.0,
    2.0,
    1.5
)

filtered = funds[
    (funds["Return (%)"] >= min_return) &
    (funds["Expense Ratio"] <= max_expense)
]

st.dataframe(filtered, use_container_width=True)

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download CSV",
    csv,
    "filtered_funds.csv",
    "text/csv"
)