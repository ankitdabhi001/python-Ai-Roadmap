from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("HuggingFace Transformers are amazing!")
print(result)
