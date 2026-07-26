import os
import matplotlib
matplotlib.use("Agg")
import pandas as pd
import matplotlib.pyplot as plt
os.makedirs("results", exist_ok=True)
train = pd.read_csv("data/train.csv")
print(train.info())
print(train.describe())
weekly_orders = (
    train.groupby("week")
    ["num_orders"]
    .sum()
)
plt.figure(figsize=(12, 6))
plt.plot(
    weekly_orders,
    color="blue"
)
plt.title("Weekly Demand Trend")
plt.xlabel("Week")
plt.ylabel("Orders")
plt.grid(True)
plt.savefig(
    "results/weekly_demand_trend.png"
)
print("Graph saved successfully")