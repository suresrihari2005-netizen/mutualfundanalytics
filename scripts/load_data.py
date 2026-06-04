import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

nav = pd.read_csv("data/proccessed/02_nav_history_cleaned.csv")
nav.to_sql("nav_history", engine, if_exists="replace", index=False)

txn = pd.read_csv("data/proccessed/08_investor_transactions_cleaned.csv")
txn.to_sql("investor_transactions", engine, if_exists="replace", index=False)

perf = pd.read_csv("data/proccessed/07_scheme_performance_cleaned.csv")
perf.to_sql("scheme_performance", engine, if_exists="replace", index=False)

print("All data loaded successfully!")