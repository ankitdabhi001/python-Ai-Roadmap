
# List of student marks
marks = [85, 90, 78, 92, 88, 76, 95]

# Print all marks
print("Student Marks:")
for m in marks:
    print(m)

# Average
avg = sum(marks) / len(marks)
print(f"\n📊 Average Marks: {avg:.2f}")

# Topper
print(f"🏆 Highest Marks: {max(marks)}")
print(f"📉 Lowest Marks: {min(marks)}")
