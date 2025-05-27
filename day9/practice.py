# contacts = {'ankit', 'ankit', 'ravi', 'meena'}

# a=sorted(contacts)
# print(a)


# Two messy friend lists
person1_friends = ['Ankit', 'Ravi', 'meena', 'Ankit', 'sohan']
person2_friends = ['Meena', 'sohan', 'RAVI', 'Simran', 'simran']

# Step 1: Clean up names (strip, title case) and remove duplicates using sets
set1 = {name.strip().title() for name in person1_friends}
set2 = {name.strip().title() for name in person2_friends}

# Step 2: Find mutual friends
mutual = set1 & set2

# Step 3: Find unique friends
unique = set1 ^ set2

# Step 4: Print results
print("👫 Mutual Friends:", sorted(mutual))
print("🌟 Unique Friends:", sorted(unique))
