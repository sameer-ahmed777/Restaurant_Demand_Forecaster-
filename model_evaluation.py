import os
import sys
from sklearn.metrics import (
    mean_absolute_percentage_error
)
sys.path.append(
    os.path.dirname(__file__)
)
from data_preprocessing import (
    load_data,
    create_features
)
df = load_data()
df = create_features(df)
df["baseline_prediction"] = (
    df["lag_1"]
)
baseline_mape = (
    mean_absolute_percentage_error(
        df["num_orders"],
        df["baseline_prediction"]
    )
)
print(
    "Baseline MAPE:",
    round(baseline_mape, 4)
)