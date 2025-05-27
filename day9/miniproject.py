raw_input = input("Enter names/items (comma-separated): ")
items = [i.strip() for i in raw_input.split(",")]
unique_sorted = sorted(set(items))
print("🧹 Clean List:", unique_sorted)
