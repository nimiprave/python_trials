import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from rich.console import Console


console = Console()

load_dotenv()
print(os.environ.get("OPENAI_API_KEY"))


model = init_chat_model("gpt-4o-mini", model_provider="openai")

messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!")
]
result_message = model.invoke(messages)
console.print(result_message)


# from openai import OpenAI
# client = OpenAI()

# response = client.responses.create(
#     model="gpt-4.1",
#     input="Write a one-sentence bedtime story about a unicorn."
# )

# print(response.output_text)
