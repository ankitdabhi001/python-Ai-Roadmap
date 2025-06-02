import openai

openai.api_key="sk-proj-TLEPVkdgxXwNF9wNKrT-ngHVhSp36Ebw0TqjqwicjFCdzto-1Yq_jD5EAMqfJlSCUgWGPZh8vXT3BlbkFJjueY0kiujAz1eyJHsmrvbqMZRQtbzme7AeNPPDql5GMmPhK_Elenkg4iEEgi8sAHlS_3vl-_gA-"

topic=input("enter your topic")

response=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"you are ai script generater"},
        {"role":"user","content":f"give a content about{topic}"}

    ]
)

answer=response['choices'][0]['message']['content']

print("your script content is given below")

print(answer)