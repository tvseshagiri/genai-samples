from pydantic import BaseModel, ConfigDict
from typing import List
import pydantic


class Config:
    arbitrary_types_allowed = True


schema = {
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
        "phone": {"type": "string"},
        "experience": {"type": "integer"},
        "education": {
            "type": "array",
            "items": {
                "course": {"type": "string"},
            },
        },
        "skills": {
            "type": "array",
            "items": {
                "skill": {"type": "string"},
            },
        },
    },
}


@pydantic.dataclasses.dataclass(config=Config)
class Resume(BaseModel):
    name: str
    email: str
    phone: str
    experience: int
    education: str
    skills: List[str]


from langchain_community.document_loaders import Docx2txtLoader


loader = Docx2txtLoader("inputs/Bhargavi_AndroidResume.docx")
docs = loader.load()

# create a list comprehension for docs
content = ""

for doc in docs:
    content += doc.page_content
from langchain_openai import ChatOpenAI
from langchain.chains import create_extraction_chain, create_extraction_chain_pydantic
from dotenv import load_dotenv

load_dotenv()

chain = create_extraction_chain(schema=schema, llm=ChatOpenAI(temperature=0))
print(chain.invoke(content)["text"])
