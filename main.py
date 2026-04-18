from dotenv import load_dotenv
import os

load_dotenv();

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
# from tavily import TavilyClient
from langchain_tavily import TavilySearch

# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches over the internet
#     Args:
#         query: The query to search for
#     Returns:
#         The search result
#     """
#     print(f"Searching for {query}")
#     # return "Tokyo weather is sunny"
#     return tavily.search(query=query)


llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0
)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from search-agent!")
    result = agent.invoke({"messages": HumanMessage(content="top 6 recent job postings in bangalore urban area for "
                                                            "java full stack developer who uses java and react")})
    print(result)


if __name__ == "__main__":
    main()
