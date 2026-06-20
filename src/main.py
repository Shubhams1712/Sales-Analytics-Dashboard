from loader import load_data
from cleaner import clean_data
from sales import calculate_sales_metrics
from visualizer import visualize_data
from exporter import export_data

def main():

    df = load_data()

    df = clean_data(df)

    df, analysis = calculate_sales_metrics(df)

    visualize_data(df, analysis)

    export_data(df, analysis)

if __name__ == "__main__":
    main()