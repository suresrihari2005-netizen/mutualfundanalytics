import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Home", layout="wide")

st.title("🏠 Home Dashboard")

st.markdown("## Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("Total Funds", "40")
col2.metric("Average Return", "14.5%")
col3.metric("Average Expense Ratio", "1.12%")

col4, col5, col6 = st.columns(3)

col4.metric("Average Sharpe", "1.41")
col5.metric("Average Alpha", "3.12")
col6.metric("Average Beta", "0.95")

st.divider()

data = pd.DataFrame({
    "Category": [
        "Equity",
        "Debt",
        "Hybrid",
        "ELSS"
    ],
    "Funds": [
        18,
        10,
        8,
        4
    ]
})

fig = px.pie(
    data,
    values="Funds",
    names="Category",
    hole=0.5,
    title="Fund Categories"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Sample Fund Data")

sample = pd.DataFrame({
    "Fund": [
        "SBI Bluechip",
        "Axis Growth",
        "HDFC Equity",
        "ICICI Value"
    ],
    "Return %": [
        18.4,
        15.2,
        16.9,
        14.8
    ],
    "Risk": [
        "Moderate",
        "High",
        "Moderate",
        "Low"
    ]
})

st.dataframe(sample, use_container_width=True)