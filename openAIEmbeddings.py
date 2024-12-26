from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
apiKey = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=apiKey)
response = client.embeddings.create(
    input="The food was delicious and the waiter...", model="text-embedding-ada-002"
)
print(response)
