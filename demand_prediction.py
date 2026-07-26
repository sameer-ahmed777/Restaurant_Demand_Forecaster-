import joblib
import pandas as pd
model = joblib.load(
    "models/demand_forecasting_model.pkl"
)
sample = pd.DataFrame({
    "week": [150],
    "checkout_price": [200],
    "base_price": [250],
    "discount": [50],
    "emailer_for_promotion": [1],
    "homepage_featured": [0],
    "category": [0],
    "cuisine": [0],
    "city_code": [647],
    "region_code": [56],
    "center_type": [0],
    "op_area": [4.5],
    "lag_1": [300]
})
prediction = model.predict(
    sample
)
print(
    "Predicted Demand:",
    int(prediction[0])
)