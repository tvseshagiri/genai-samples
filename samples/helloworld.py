from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI

prompt = PromptTemplate.from_template("What is the capital city of Germany?")

llm = GoogleGenerativeAI(model="gemini-pro")
response = llm.invoke(prompt.format())
print(response)
