from dotenv import load_dotenv
import os

load_dotenv();

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama


@tool
def search(query: str) -> str:
    """
    Tool that searches over the internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return "Tokyo weather is sunny"


llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0
)
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from search-agent!")
    result = agent.invoke({"messages": HumanMessage(content="What is the weather in tokyo?")})
    print(result)


if __name__ == "__main__":
    main()
