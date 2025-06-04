import pandas as pd
import os
# from gpt4all import GPT4All  # Uncomment if using GPT4All

def excel_to_csv_converter(file_path):
    # Check if it's an Excel file
    if not file_path.endswith((".xlsx", ".xls")):
        print("❌ Error: Not an Excel file")
        return
    
    # Load Excel file
    df = pd.read_excel(file_path)

    # Clean data (remove empty rows/columns)
    df.dropna(how='all', inplace=True)  # Remove empty rows
    df.dropna(axis=1, how='all', inplace=True)  # Remove empty columns

    # Save as CSV
    csv_file = os.path.splitext(file_path)[0] + ".csv"
    df.to_csv(csv_file, index=False)

    print(f"✅ Converted to CSV: {csv_file}")
    return df, csv_file

# ✅ Usage Example
excel_path = "E:/Python Roadmap/python-Ai-Roadmap/day17/sample_sales.xlsx"
df, csv_path = excel_to_csv_converter(excel_path)
