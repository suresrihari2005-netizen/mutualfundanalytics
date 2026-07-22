import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💰 Capital Allocation")

df = pd.DataFrame({
    "Category":["Equity","Debt","Gold","Hybrid"],
    "Allocation":[60,20,10,10]
})

fig = px.bar(
    df,
    x="Category",
    y="Allocation",
    text="Allocation"
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(df, use_container_width=True)