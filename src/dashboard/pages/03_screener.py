import streamlit as st
import pandas as pd

st.set_page_config(page_title="Screener", layout="wide")

st.title("🔍 Fund Screener")

data = pd.DataFrame({
    "Fund": ["SBI Bluechip", "Axis Growth", "HDFC Equity", "ICICI Value"],
    "Return (%)": [18.4, 15.2, 16.9, 14.8],
    "Risk": ["Moderate", "High", "Moderate", "Low"],
    "Expense Ratio": [1.20, 1.05, 1.10, 0.95]
})

min_return = st.slider("Minimum Return (%)", 0, 25, 10)

filtered = data[data["Return (%)"] >= min_return]

st.dataframe(filtered, use_container_width=True)

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download CSV",
    csv,
    file_name="filtered_funds.csv",
    mime="text/csv"
)