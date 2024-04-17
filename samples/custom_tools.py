from langchain.chains.llm_math.base import LLMMathChain
from langchain.agents import Tool


def create_math_tool(llm):
    # initialize the math chain
    llm_math = LLMMathChain(llm=llm)

    # initialize the math tool
    math_tool = Tool(
        name="Calculator",
        func=llm_math.run,
        description="Useful to answer questions about math.",
    )


def create_general_tool(llm):
    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain

    prompt = PromptTemplate(input_variables=["query"], template="{query}")

    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # initialize the LLM tool
    llm_tool = Tool(
        name="Language Model",
        func=llm_chain.run,
        description="use this tool for general purpose queries and logic",
    )

    return llm_tool


# Creating our own tool with @tool decorator

from langchain.tools import tool


@tool
def greeting_tool(name: str) -> str:
    """Use this tool for greeting"""
    return "Hello!!! " + name
