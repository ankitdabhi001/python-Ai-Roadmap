import pandas as pd

data = pd.read_csv("sample_dataset.csv")
print("📊 Summary Stats")
print(data)

print("\n🏅 Top Performers")
# print(data.sort_values(by="Age").head(3))
data=data.drop_duplicates
print(data)