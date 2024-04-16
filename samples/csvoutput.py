from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)


output_parser = CommaSeparatedListOutputParser()

format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    template="List last Cricket One day World cup winning team details.\n{format_instructions}",
    partial_variables={"format_instructions": format_instructions},
    input_variables=[],
)

model = ChatOpenAI(temperature=0)

chain = prompt | model | output_parser

resp = chain.invoke({})

print(resp)
