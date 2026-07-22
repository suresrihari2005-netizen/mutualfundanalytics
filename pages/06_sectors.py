
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏢 Sector Analysis")

df = pd.DataFrame({
    "Sector":["Large Cap","Mid Cap","Small Cap","Flexi Cap"],
    "Funds":[18,14,10,8]
})

fig = px.pie(
    df,
    names="Sector",
    values="Funds",
    title="Sector Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(df, use_container_width=True)