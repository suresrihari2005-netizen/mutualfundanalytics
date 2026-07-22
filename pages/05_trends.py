import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Trends", layout="wide")

st.title("📈 Trends Analysis")

df = pd.DataFrame({
    "Year":[2020,2021,2022,2023,2024],
    "Return":[12,15,18,16,21]
})

fig = px.line(
    df,
    x="Year",
    y="Return",
    markers=True,
    title="Fund Return Trend"
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(df, use_container_width=True)