import pandas as pd

def export_data(df, analysis):
    try:
        df.to_csv("output/sales_analytics.csv", index = False)
        print("Cleaned data saved successfully")
    except FileNotFoundError:
        print("File not found")

    with open("output/report.txt", "w") as file:
        file.write("====== Sales Analytics Report ======\n\n")
        file.write(f"Total Orders: {len(df)}\n")
        file.write("\n")
        file.write(f"Total Revenue: {analysis['total_revenue']}\n")
        file.write("\n")
        file.write(f"Average Order Value: {analysis['avg_order_value']}\n")
        file.write("\n")
        file.write(f"Highest Sale: {analysis['highest_sale']}\n")
        file.write("\n")
        file.write(f"Lowest Sale: {analysis['lowest_sale']}\n")
        file.write("\n")
        file.write(f"Highest Spending Customer:\n{analysis['top_customers'].head(1).to_string()}\n")
        file.write("\n")
        file.write(f"Top 5 Product: {analysis['top_products'].to_string()}\n")
        file.write("\n")
        file.write("Revenue by Category:\n")
        file.write(analysis['category_sales'].to_string())
        file.write("\n\n")
        file.write("Revenue by Region:\n")
        file.write(analysis['region_sales'].to_string())
        file.write("\n\n")
        file.write("\n\nMonthly Sales:\n")
        file.write(analysis['monthly_sales'].to_string())

        print("Sales report generated successfully.")
        
