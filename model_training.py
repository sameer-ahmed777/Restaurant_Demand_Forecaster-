import os
import sys
import joblib
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_absolute_percentage_error
sys.path.append(
    os.path.dirname(__file__)
)
from data_preprocessing import (
    load_data,
    create_features
)
# Load Data
df = load_data()
df = create_features(df)
# Encode categorical columns
categorical_columns = [
    "category",
    "cuisine",
    "center_type"
]

for column in categorical_columns:

    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(
        df[column]
    )

# Features
features = [
    "week",
    "checkout_price",
    "base_price",
    "discount",
    "emailer_for_promotion",
    "homepage_featured",
    "category",
    "cuisine",
    "city_code",
    "region_code",
    "center_type",
    "op_area",
    "lag_1"
]
X = df[features]
y = df["num_orders"]
# Time Series Split
tscv = TimeSeriesSplit(
    n_splits=5
)
# Random Forest Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
scores = []
for train_idx, test_idx in tscv.split(X):

    X_train = X.iloc[train_idx]
    X_test = X.iloc[test_idx]

    y_train = y.iloc[train_idx]
    y_test = y.iloc[test_idx]
    model.fit(
        X_train,
        y_train
    )
    predictions = model.predict(
        X_test
    )
    mape = mean_absolute_percentage_error(
        y_test,
        predictions
    )
    scores.append(mape)
# Average MAPE
average_mape = round(
    sum(scores) / len(scores),
    4
)
print(
    "Average MAPE:",
    average_mape
)
# Create Results Folder
os.makedirs(
    "results",
    exist_ok=True
)
# Actual vs Predicted Graph
plt.figure(
    figsize=(10, 5)
)
plt.plot(
    y_test.values[:100],
    label="Actual Demand",
    linewidth=2
)
plt.plot(
    predictions[:100],
    label="Predicted Demand",
    linewidth=2
)
plt.title(
    "Actual vs Predicted Demand"
)
plt.xlabel(
    "Samples"
)
plt.ylabel(
    "Number of Orders"
)
plt.legend()
plt.tight_layout()
plt.savefig(
    "results/actual_vs_predicted.png"
)
plt.close()
print(
    "Actual vs Predicted graph saved."
)
# Train Final Model On Full Dataset
model.fit(
    X,
    y
)
# Save Model
os.makedirs(
    "models",
    exist_ok=True
)
joblib.dump(
    model,
    "models/demand_forecasting_model.pkl"
)
print(
    "Model saved successfully."
)