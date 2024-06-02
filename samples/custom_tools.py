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
        name="Language_Model",
        func=llm_chain.run,
        description="use this tool for general purpose queries and logic",
    )
    print(llm_tool)
    return llm_tool


# Creating our own tool with @tool decorator

from langchain.tools import tool
import random


@tool
def greeting_tool(name: str) -> str:
    """Use this tool for greeting"""
    return "Hello!!! " + name


@tool
def order_status_checking_tool(order_number: str) -> str:
    """Use this tool for checking status of an order by order number"""
    order_statues = ["Completed", "Delivered", "In Progress"]

    # Randomly select one of the order statuses
    import random

    return "Your order {order_number} is {status} ".format(
        order_number=order_number, status=random.choice(order_statues)
    )
