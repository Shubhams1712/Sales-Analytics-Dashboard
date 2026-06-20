import pandas as pd

def load_data():
    try:
        data = pd.read_csv("data/inventory.csv")
        # print(data.to_string())
        print("File loaded successfully")
        return data
    except FileNotFoundError:
        print("File not found.")
    except Exception:
        print("Unknown Error")
