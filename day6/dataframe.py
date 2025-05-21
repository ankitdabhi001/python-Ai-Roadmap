import pandas as pd

df=pd.read_csv("data.csv")

print(df.head(3))

print("total entri",len(df))
print(f"average",df.mean(numeric_only=True))
print(f"minn",df.min(numeric_only=True))
print(f"maxx",df.max(numeric_only=True))

if 'Amount' in df.columns:
    print(df.sort_values(by='Amount',ascending=False).head(3))