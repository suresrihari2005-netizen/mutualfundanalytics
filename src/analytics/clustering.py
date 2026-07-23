import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample financial data
df = pd.DataFrame({
    "company_id": [1, 2, 3, 4, 5],
    "company_name": [
        "ABC Ltd",
        "XYZ Industries",
        "Future Tech",
        "Prime Finance",
        "Green Energy"
    ],
    "return_on_equity_pct": [18, 12, 24, 10, 20],
    "debt_to_equity": [0.4, 1.2, 0.3, 2.0, 0.5],
    "revenue_cagr_5yr": [15, 10, 22, 6, 18],
    "fcf_cagr_5yr": [12, 8, 20, 4, 16],
    "operating_profit_margin_pct": [20, 12, 28, 8, 24]
})

features = [
    "return_on_equity_pct",
    "debt_to_equity",
    "revenue_cagr_5yr",
    "fcf_cagr_5yr",
    "operating_profit_margin_pct"
]

# Standardize the features
scaler = StandardScaler()
scaled = scaler.fit_transform(df[features])

# KMeans clustering
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df["cluster_id"] = kmeans.fit_predict(scaled)

# Cluster names
cluster_names = {
    0: "High Quality",
    1: "Growth",
    2: "Value",
    3: "Turnaround",
    4: "Dividend"
}

df["cluster_name"] = df["cluster_id"].map(cluster_names)

# Distance from centroid
distances = kmeans.transform(scaled)
df["distance_from_centroid"] = [
    round(distances[i][cluster], 3)
    for i, cluster in enumerate(df["cluster_id"])
]

# Save output
os.makedirs("output", exist_ok=True)

output = df[
    [
        "company_id",
        "cluster_id",
        "cluster_name",
        "distance_from_centroid"
    ]
]

output.to_csv("output/cluster_labels.csv", index=False)

print("\n===== Cluster Labels =====")
print(output)

print("\nDay 36 Completed Successfully!")
print("Saved: output/cluster_labels.csv")