from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
# Web Search Agent
web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

# run the agent with a query
query = input("What is your question?:   ")
while query.upper() != 'EXIT':
    # web_agent.print_response("Whats happening in France?", stream=True)
    web_agent.print_response(query, stream=True)
    query = input("What is your question?:   ")
