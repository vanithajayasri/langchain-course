import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()


@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search results
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query, num_results=3)


llm = ChatOpenAI(model="gpt-5-mini")
tools = [TavilySearch()]
agent = create_agent(llm, tools=tools)

def main():
    print("Hello from lang-chian course")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")})
    print(result)


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.
#     information = """
#     Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and entrepreneur known for his leadership of Tesla, SpaceX, Twitter, and xAI. Musk has been the wealthiest person in the world since 2025; as of February 2026, Forbes estimates his net worth to be around US$852 billion.
#
# Born into a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. Musk also became an American citizen in 2002.
#     """
#
#
#     summary_template = """
#     given the information {information} about a person, I want you to create:
#     1. A short summary
#     2. two interesting facts about them
#     """
#
#     summary_prompt_template = PromptTemplate(
#         input_variables=["information"],
#         template=summary_template
#     )
#
#     llm = ChatOpenAI(temperature=0, model="gpt-5-mini")
#     #llm = ChatOllama(temperature=0, model="llama3.2")
#
#     chain = summary_prompt_template | llm
#     response = chain.invoke(input={"information": information})
#     print(response.content)

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
