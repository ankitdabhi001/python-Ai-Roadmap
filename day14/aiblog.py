import openai
import os

openai.api_key = "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" # Paste your real key here



def generate_blog_post(topic):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # You can change to "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful tech blogger."},
            {"role": "user", "content": f"Write a beginner-friendly blog post about: {topic}. Keep it under 100 words, include headings, and write in Markdown format."}
        ],
        temperature=0.7,
        max_tokens=700
    )
    return response.choices[0].message.content

# --- MAIN ---
if __name__ == "__main__":
    topic = input("📝 Enter a blog topic: ")
    print("\n⏳ Generating blog post...")
    blog_post = generate_blog_post(topic)
    print("\n✅ Blog Post Generated:\n")
    print(blog_post)
