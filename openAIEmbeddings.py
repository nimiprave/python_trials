from openai import OpenAI
from transform

apiKey = "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"
client = OpenAI(api_key=apiKey)
response = client.embeddings.create(
    input="The food was delicious and the waiter...", model="text-embedding-ada-002"
)
print(response)

