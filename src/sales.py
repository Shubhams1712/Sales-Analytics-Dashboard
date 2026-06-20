
def calculate_sales_metrics(df):

    df["Cost_Price"] = df["Unit_Price"] * 0.7
    df["Total_Cost"] = df["Cost_Price"] * df["Quantity"]
    df["Revenue_After_Discount"] = (df["Total_Sales"] - (df["Total_Sales"] * df["Discount"] / 100))
    df["Profit"] = (df["Revenue_After_Discount"] - df["Total_Cost"])
    df["Profit_Margin"] = (df["Profit"] / df["Revenue_After_Discount"]) * 100

    analysis = {
    "total_revenue": df["Revenue_After_Discount"].sum().round(2),
    "total_profit": df["Profit"].sum().round(2),
    "avg_order_value": df["Revenue_After_Discount"].mean().round(2),
    "average_profit": df["Profit"].mean().round(2),
    "average_profit_margin": df["Profit_Margin"].mean().round(2),
    "top_customers": get_top_customers(df),
    "top_products": get_top_products(df),
    "region_sales": get_region_wise_sales(df),
    "category_sales": get_category_wise_sales(df),
    "monthly_sales": get_monthly_sales(df),
    "highest_sale": df["Revenue_After_Discount"].max(),
    "lowest_sale": df["Revenue_After_Discount"].min()
    }

    return df, analysis

def get_top_customers(df):
    top_customers = (df.groupby("Customer_Name")["Revenue_After_Discount"].sum().sort_values(ascending = False).head(10))
    return top_customers

def get_top_products(df):
    top_products = (df.groupby("Product")["Revenue_After_Discount"].sum().sort_values(ascending = False).head(5))
    return top_products

def get_region_wise_sales(df):
    region_sales = (df.groupby("Region")["Revenue_After_Discount"].sum().sort_values(ascending = False))
    return region_sales

def get_category_wise_sales(df):
    category_sales = (df.groupby("Category")["Revenue_After_Discount"].sum().sort_values(ascending = False))
    return category_sales

def get_monthly_sales(df):
    monthly_sales = (df.groupby(df["Order_Date"].dt.to_period("M"))["Revenue_After_Discount"].sum())
    return monthly_sales
