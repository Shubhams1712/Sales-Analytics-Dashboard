import pandas as pd

def analyze_data(df):

    df["Performance_Score"] = (df["Tasks_Completed"] * 2 + df["Working_Hours"] * 0.5 + df["Rating"] * 20 - df["Leaves"] * 5 + df["Overtime_Hours"] * 1.5)
    df["Performance_Category"] = "Needs Improvement"
    df.loc[df["Performance_Score"] >= 150, "Performance_Category"] = "Average"
    df.loc[df["Performance_Score"] >= 200, "Performance_Category"] = "Good"
    df.loc[df["Performance_Score"] >= 250, "Performance_Category"] = "Excellent"

    analysis = {
        "total_employees": len(df),
        "average_salary": df["Salary"].mean().round(2),
        "highest_salary": df["Salary"].max(),
        "lowest_salary": df["Salary"].min(),
        "average_rating": df["Rating"].mean().round(2),
        "average_leaves": df["Leaves"].mean().round(2),
        "average_overtime": df["Overtime_Hours"].mean().round(2),
        "department_employee_count": df["Department"].value_counts(),
        "department_average_salary": df.groupby("Department")["Salary"].mean().round(2),
        "top10": df.sort_values("Rating", ascending=False).head(10)[["Employee_ID", "Name", "Department", "Rating"]],
        "bottom10": df.sort_values("Rating").head(10),
        "top_performers": df.sort_values("Performance_Score", ascending=False).head(10)
    }
    return df, analysis
