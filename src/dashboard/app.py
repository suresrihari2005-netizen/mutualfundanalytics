import streamlit as st

st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Mutual Fund Analytics Dashboard")

st.sidebar.success("Select a page from the sidebar.")

st.markdown("""
Welcome to the Mutual Fund Analytics Dashboard.

Use the pages on the left to explore:

- Home
- Company Profile
- Screener
- Peer Comparison
- Trends
- Sector Analysis
- Capital Allocation
- Reports
""")