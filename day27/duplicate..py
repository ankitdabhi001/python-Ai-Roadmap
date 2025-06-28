nums = [1,2,3,4,5,5,4,1]

a = set([b for b in nums if nums.count(b)>1])

print(f"Duplicate Is : {a}")