import pandas as pd

data = pd.read_csv("sample_dataset.csv")
print("📊 Summary Stats")
print(data)

unique_data=data.drop_duplicates(subset=["Name"])

print("\n🏅 Top Performers")
print(unique_data.sort_values(by="Age").head(3))

