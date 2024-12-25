from transformers import pipeline
from PIL import Image

pipe = pipeline("document-question-answering",
                model="naver-clova-ix/donut-base-finetuned-docvqa")

question = "What is the total amount?"
image = Image.open("Costo.jpeg")

pipe(image=image, question=question)

# [{'answer': '20,000$'}]
