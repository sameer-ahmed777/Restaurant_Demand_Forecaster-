from sklearn.metrics import mean_absolute_percentage_error
from data_preprocessing import (
    load_data,
    create_features
)
# Load and prepare data
df = load_data()
df = create_features(df)
print("\nCategory Wise MAPE Report")
print("-" * 40)
# Calculate MAPE for each category
for category in df["category"].unique():
    temp = df[
        df["category"] == category
    ]
    mape = mean_absolute_percentage_error(
        temp["num_orders"],
        temp["lag_1"]
    )
    print(
        f"{category} : {round(mape, 4)}"
    )