
from openai import OpenAI

# Create client instance
client = OpenAI(api_key="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")

def improve_resume(resume_text):
    prompt = f"""
    Please improve the following resume text by making it more professional, concise, and keyword-rich for job applications:

    {resume_text}

    Provide the improved version only.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that improves resumes."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7,
    )

    improved_text = response.choices[0].message.content.strip()
    return improved_text

# Example usage
original_resume = """
Name: Ankit
Email: ankit@example.com
Skills:
- Python
- AI
- Data Analysis
Experience:
- Intern at TCS
- Freelancer at Upwork
"""

improved_resume = improve_resume(original_resume)
print("Improved Resume:\n", improved_resume)

