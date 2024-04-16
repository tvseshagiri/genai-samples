from typing import List
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)


# Pydantic Model
class Country(BaseModel):
    country: str = Field(description="Name of the country")
    capital_city: str = Field(description="Capital City of Country")


# Model parser
parser = JsonOutputParser(pydantic_object=Country)

prompt = PromptTemplate(
    template="{format_instructions}\n What is the capital city of {country}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | llm | parser

resp = chain.invoke({"country": "India"})

print(parser.get_format_instructions())
print(resp)
