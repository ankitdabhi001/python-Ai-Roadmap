import random

# Sample Q&A bank
qa_bank = [
    {
        "question": "What is a Python decorator?",
        "answer": "A decorator in Python is a function that modifies another function without changing its code. It is commonly used for logging, access control, and memoization."
    },
    {
        "question": "Explain list vs tuple in Python.",
        "answer": "Lists are mutable and tuples are immutable. Lists are defined using [], while tuples use ()."
    },
    {
        "question": "What is the difference between 'is' and '==''?",
        "answer": "'==' checks for value equality, whereas 'is' checks for object identity (whether they point to the same memory)."
    },
    {
        "question": "What are Python's data types?",
        "answer": "Common data types are int, float, str, list, tuple, set, dict, and bool."
    },
    {
        "question": "How does Python manage memory?",
        "answer": "Python uses reference counting and garbage collection to manage memory."
    }
]

# Select 3 random questions
selected = random.sample(qa_bank, 3)

print("🧠 Welcome to Interview Buddy AI!")
print("You will be asked 3 Python interview questions. Type your answer and compare with the expert response.\n")

for i, qa in enumerate(selected, 1):
    print(f"🔹 Question {i}: {qa['question']}")
    user_input = input("📝 Your Answer: ")
    print("✅ Sample Answer:", qa["answer"])
    print("-" * 50)

print("\n🎯 Great job! Review your responses and keep practicing!")
