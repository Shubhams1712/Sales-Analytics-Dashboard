import matplotlib.pyplot as plt

def visualize_data(df, analysis):
    
    category_revenue = analysis["category_sales"]
    bars = plt.bar(category_revenue.index, category_revenue.values, color="royalblue")
    for bar in bars:
        plt.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height(),
            f"{bar.get_height():.0f}",
            ha="center",
            va="bottom",
            fontsize=9
        )
    plt.title("Revenue by Category")
    plt.xlabel("Product Category")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("output/charts/revenue_by_category.png")
    plt.close()

    region_revenue = analysis["region_sales"]
    bars = plt.bar(region_revenue.index, region_revenue.values, color = "seagreen")
    for bar in bars:
        plt.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height(),
            f"{bar.get_height():.0f}",
            ha="center",
            va="bottom",
            fontsize=9
        )
    plt.title("Revenue by region")
    plt.xlabel("Region")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("output/charts/revenue_by_region.png")
    plt.close()

    monthly_revenue = analysis["monthly_sales"]
    plt.figure(figsize=(8,5))
    plt.plot(monthly_revenue.index.strftime("%b"), monthly_revenue.values, marker="o", color="darkorange", linewidth=2)
    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("output/charts/monthly_revenue.png")
    plt.close()

    top_customer = analysis["top_customers"]
    plt.barh(top_customer.index, top_customer.values, color = "mediumorchid")
    plt.title("Top Customers")
    plt.xlabel("Revenue")
    plt.ylabel("Customer")
    plt.tight_layout()
    plt.savefig("output/charts/top_customers.png")
    plt.close()
    
    top_products = analysis["top_products"]
    plt.barh(top_products.index, top_products.values, color = "teal")
    plt.title("Revenue")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("output/charts/top_products.png")
    plt.close()

    plt.figure(figsize=(8,5))
    discount = df["Discount"].value_counts().sort_index()
    plt.bar(discount.index.astype(str), discount.values, color = "tomato")
    plt.title("Discount Distribution")
    plt.xlabel("Discount (%)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("output/charts/discount_distribution.png")
    plt.close()

    plt.figure(figsize=(8,5))
    plt.scatter(df["Quantity"], df["Total_Sales"], color="crimson", alpha=0.7)
    plt.title("Quantity vs Total Sales")
    plt.xlabel("Quantity")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.savefig("output/charts/quantity_vs_sales.png")
    plt.close()
