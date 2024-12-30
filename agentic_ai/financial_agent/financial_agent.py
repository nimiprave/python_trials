# create application for multiple agents
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.google import Gemini
from dotenv import load_dotenv
# import openai
import os

load_dotenv()

# create web search agent
web_search_agent = Agent(
    name='web_search_agent',
    role='Search the web for the information',
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tool=DuckDuckGo(),
    instructions=['Always include the source'],
    show_tool_calls=True,
    markdown=True

)


# create financial agent
finance_agent = Agent(
    name='Finance AI agent',
    model=Gemini(id="gemini-1.5-flash"),
    # model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,
                         stock_fundamentals=True, company_news=True, company_info=True)],
    show_tool_calls=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=[
        "Format your response using markdown and use tables to display data where possible."],
)

# multi agent application
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Gemini(id="gemini-1.5-flash"),
    instructions=["Use the web search agent to find information about the company and the financial agent to find information about the stock.",
                  "Use table to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Setup the app as chat via cmd
if __name__ == "__main__":
    query = input("Enter the Query:  ")
    while query.upper() != "EXIT":
        multi_ai_agent.print_response(query, stream=True)
        query = input("Enter the Query:  ")


# multi_ai_agent.print_response(
#     "Summarize analyst recommendations for BCE Inc and share the market news.", stream=True)
