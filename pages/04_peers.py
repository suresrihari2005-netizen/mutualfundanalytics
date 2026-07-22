import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Peer Comparison", layout="wide")

st.title("📊 Peer Comparison")

df = pd.DataFrame({
    "Fund": [
        "SBI Bluechip",
        "Axis Growth",
        "HDFC Equity",
        "ICICI Value",
        "Parag Parikh"
    ],
    "Return (%)": [
        18.4,
        15.2,
        16.9,
        14.8,
        21.3
    ]
})

fig = px.bar(
    df,
    x="Fund",
    y="Return (%)",
    text="Return (%)",
    title="Fund Return Comparison"
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(df, use_container_width=True)