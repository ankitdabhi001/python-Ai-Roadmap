# Sample candidate skill lists
candidate_1 = ["Python", "Machine Learning", "SQL", "Git"]
candidate_2 = ["Java", "python", "SQL", "Docker"]

# Clean and convert to sets (for intersection)
skills_1 = set(skill.strip().title() for skill in candidate_1)
skills_2 = set(skill.strip().title() for skill in candidate_2)

# Find common skills
common_skills = skills_1 & skills_2

# Display results
print("🤝 Common Skills Between Candidates:")
if common_skills:
    for skill in sorted(common_skills):
        print(f"✅ {skill}")
else:
    print("❌ No common skills found.")
