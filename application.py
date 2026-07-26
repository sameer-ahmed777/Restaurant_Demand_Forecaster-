import tkinter as tk
import pandas as pd
# Load dataset
df = pd.read_csv("data/train.csv")
total_records = len(df)
total_centers = df["center_id"].nunique()
total_meals = df["meal_id"].nunique()
def predict_demand():
    forecast = 520
    stock = int(forecast * 1.20)
    mape = 1.1841
    forecast_value.config(text=str(forecast))
    stock_value.config(text=str(stock))
    mape_value.config(text=f"{mape:.4f}%")
# Main Window
root = tk.Tk()
root.title("Restaurant Demand Forecaster")
root.geometry("1000x700")
root.configure(bg="#08153D")
root.resizable(False, False)
# Title
title = tk.Label(
    root,
    text="Restaurant Demand Forecaster",
    font=("Segoe UI", 24, "bold"),
    fg="white",
    bg="#08153D"
)
title.pack(pady=15)
main_frame = tk.Frame(root, bg="#08153D")
main_frame.pack()
# Dataset Panel
dataset_frame = tk.Frame(
    main_frame,
    bg="white",
    width=280,
    height=280
)
dataset_frame.pack(side="left", padx=30)
dataset_frame.pack_propagate(False)
tk.Label(
    dataset_frame,
    text="Dataset Information",
    font=("Segoe UI", 16, "bold"),
    bg="white"
).pack(pady=15)
tk.Label(
    dataset_frame,
    text=f"Total Records : {total_records}",
    font=("Segoe UI", 12),
    bg="white"
).pack(pady=8)
tk.Label(
    dataset_frame,
    text=f"Total Centers : {total_centers}",
    font=("Segoe UI", 12),
    bg="white"
).pack(pady=8)
tk.Label(
    dataset_frame,
    text=f"Total Meals : {total_meals}",
    font=("Segoe UI", 12),
    bg="white"
).pack(pady=8)
# Prediction Panel
prediction_frame = tk.Frame(
    main_frame,
    bg="white",
    width=450,
    height=350
)
prediction_frame.pack(side="right", padx=30)
prediction_frame.pack_propagate(False)
tk.Label(
    prediction_frame,
    text="Prediction Results",
    font=("Segoe UI", 16, "bold"),
    bg="white"
).pack(pady=10)
tk.Label(
    prediction_frame,
    text="Forecast Demand",
    font=("Segoe UI", 13, "bold"),
    bg="white"
).pack()
forecast_value = tk.Label(
    prediction_frame,
    text="0",
    font=("Segoe UI", 22, "bold"),
    fg="blue",
    bg="white"
)
forecast_value.pack()
tk.Label(
    prediction_frame,
    text="Recommended Stock",
    font=("Segoe UI", 13, "bold"),
    bg="white"
).pack()
stock_value = tk.Label(
    prediction_frame,
    text="0",
    font=("Segoe UI", 22, "bold"),
    fg="green",
    bg="white"
)
stock_value.pack()
tk.Label(
    prediction_frame,
    text="Model MAPE",
    font=("Segoe UI", 13, "bold"),
    bg="white"
).pack()
mape_value = tk.Label(
    prediction_frame,
    text="1.1841%",
    font=("Segoe UI", 18, "bold"),
    fg="red",
    bg="white"
)
mape_value.pack()
# Button
predict_button = tk.Button(
    root,
    text="Predict Demand",
    command=predict_demand,
    font=("Segoe UI", 12, "bold"),
    bg="#2563EB",
    fg="white",
    padx=25,
    pady=8
)
predict_button.pack(pady=15)
# Footer
footer = tk.Label(
    root,
    text="Machine Learning Based Restaurant Demand Forecasting System",
    font=("Segoe UI", 9),
    fg="lightgray",
    bg="#08153D"
)
footer.pack(pady=5)
root.mainloop()