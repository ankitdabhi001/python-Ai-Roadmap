from transformers import pipeline

# give task to a transformer

create=pipeline('text-generation',model="gpt2")

# Give topic from user :
topic=input("enter your blog topic : ")

# generate answer using proper syntax:
answer=create(topic,max_length=100,num_return_sequences=1)

# print answer
print(answer[0]['generated_text'])