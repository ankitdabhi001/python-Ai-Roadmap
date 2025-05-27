contact_a=['ankit','mayur','pratik']
contact_b=['mayur','sumit','sandip','pratik']

clean_a={name.strip().title() for name in contact_a}
clean_b={name.strip().title() for name in contact_b}

unique=clean_a | clean_b
print("unique contact is here : ",unique)

common= clean_a & clean_b
print("common contact is here : ",common)

# print(sorted(clean_a))
# print(sorted(clean_b))