import pandas as pd
def load_data():
    train = pd.read_csv("data/train.csv")
    meal = pd.read_csv("data/meal_info.csv")
    center = pd.read_csv("data/fulfilment_center_info.csv")
    df = train.merge(meal, on="meal_id")
    df = df.merge(center, on="center_id")
    return df
def create_features(df):
    df["discount"] = (
        df["base_price"] -
        df["checkout_price"]
    )
    df = df.sort_values(
        ["meal_id", "week"]
    )
    df["lag_1"] = (
        df.groupby("meal_id")["num_orders"]
        .shift(1)
    )
    df.dropna(inplace=True)
    return df
if __name__ == "__main__":
    df = load_data()
    df = create_features(df)
    print(df.head())
    print(df.shape)