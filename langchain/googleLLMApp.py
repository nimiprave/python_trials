# App for using the Langchain with the integration model for Googl Vertex AI

from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import SystemMessage, HumanMessage

# Create a new instance of the ChatVertex AI

model = ChatVertexAI(model="gemini-1.5-flash")
messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]

model.invoke(messages)
