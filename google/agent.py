from samples.custom_tools import (
    create_general_tool,
    create_math_tool,
    greeting_tool,
    order_status_checking_tool,
)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import hub
from langchain.agents import (
    AgentExecutor,
    create_tool_calling_agent,
    create_openai_functions_agent,
)

prompt = hub.pull("hwchase17/openai-tools-agent")

llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-1.5-pro")


math_tool = create_math_tool(llm)
general_tool = create_general_tool(llm)

tools = [
    greeting_tool,
    general_tool,
    order_status_checking_tool,
]

# Construct the tool calling agent
agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke(
    {
        "input": "Where is order with number 3456, If the order is in Delivered, send a completed mail"
    }
)
