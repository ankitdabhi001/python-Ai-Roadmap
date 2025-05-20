import random

# List of funny jokes
jokes = [
    "Why did the computer go to therapy? It had too many bytes of trauma! 😂",
    "Why do Java developers wear glasses? Because they can't C#! 🤓",
    "Why was the math book sad? It had too many problems. 😢",
    "Why don’t scientists trust atoms? Because they make up everything! 🧪",
    "I told my computer I needed a break... now it won’t stop sending me vacation ads. 🏖️",
    "Debugging: Being the detective in a crime movie where you are also the murderer. 🔍",
    "Why did the Python developer go broke? Because his code didn’t have any class! 🐍",
]

# Print 5 random jokes using a loop
print("🤣 Get ready to laugh! 🤣\n")
for i in range(5):
    joke = random.choice(jokes)
    print(f"{i+1}. {joke}\n")
