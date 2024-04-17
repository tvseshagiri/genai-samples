from langchain_openai import OpenAI
from langchain.agents import load_tools, initialize_agent
from custom_tools import create_math_tool, create_general_tool, greeting_tool

llm = OpenAI(temperature=0)

math_tool = create_math_tool(llm)

# when giving tools to LLM, we must pass as list of tools
tools = [math_tool]

# load the tool
tools = load_tools(["llm-math"], llm=llm)

### Let us add another tool for generic queries to the list of tools

# general_tool = create_general_tool(llm)

# tools.append(general_tool)
# tools.append(greeting_tool)

# initialize the agent
super_agent = initialize_agent(
    agent="zero-shot-react-description",
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3,
)

print(super_agent("What is 2 + 2 * 8?"))

# super_agent(
#     "if Mary has four apples and Giorgio brings two and a half apple "
#     "boxes (apple box contains eight apples), how many apples do we "
#     "have?"
# )

# super_agent("Write a Poem on Cricket")
# super_agent("Greet Sri Ram")
