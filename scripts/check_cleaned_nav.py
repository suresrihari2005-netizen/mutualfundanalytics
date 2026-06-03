import pandas as pd

df = pd.read_csv("data/proccessed/02_nav_history_cleaned.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())