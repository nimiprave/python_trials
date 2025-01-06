# App for using the Langchain with the integration model for Googl Vertex AI

from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

# Create a new instance of the ChatVertex AI
model = ChatGroq(model="llama3-groq-70b-8192-tool-use-preview")
system_message = SystemMessage(
    "Translate the following from English into Italian")
# messages = [
#     SystemMessage("Translate the following from English into Italian"),
#     HumanMessage("translate the following into italian  --- Hi!")
# ]
messages = []
human_message = input("Enter the text for translation:? ")
while human_message.upper() != "EXIT":
    messages.append(HumanMessage(human_message))
    messages.append(system_message)
    response = model.invoke(messages)
    print(response.content)
    messages.clear()
    human_message = input("Enter a message: ")


# print(response.content)
# print(model.invoke(messages))
