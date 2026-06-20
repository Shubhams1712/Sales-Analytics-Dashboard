import pandas as pd
import datetime

def clean_data(df):
    df = df.drop_duplicates().copy()

    condition1 = df["Discount"] <= 0
    condition2 = df["Unit_Price"] <= 0
    condition3 = df["Quantity"] <= 0
    condition4 = df["Total_Sales"] <= 0
    indication = condition1 | condition2 | condition3 | condition4

    df = df[~indication].copy()

    df["Order_Date"] = pd.to_datetime(df["Order_Date"])

    return df