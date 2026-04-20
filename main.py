from dotenv import load_dotenv
import os

load_dotenv();

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
# from tavily import TavilyClient
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field
from typing import List

class Source(BaseModel):
    """Schema for a sourced used by the agent"""
    url:str = Field(description="The URL from source")

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer:str = Field(description="this is agent's answer to the query")
    sources:List[Source] = Field(default_factory=list, description="The list of sources used to generate the answers")

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
    # model="llama3.2:latest" -> isn't supporting the structured output feature
    model="qwen2.5:1.5b"
)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello from search-agent!")
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings with the link to apply for java full stack developer who uses react and java")})
    print(result)
    # structured: AgentResponse = result["structured_response"]
    # print("Answer:", structured.answer)
    # for source in structured.sources:
    #     print(" -", source.url)


if __name__ == "__main__":
    main()
