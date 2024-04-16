from langchain.chains import RetrievalQA
from langchain_community.vectorstores.chroma import Chroma

from dotenv import load_dotenv
from langchain_openai.llms import OpenAI
from langchain_openai import OpenAIEmbeddings


import os

load_dotenv()


def qa_bot(qry):
    embeddings = OpenAIEmbeddings()

    docsearch = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
    )

    return qa.invoke(qry)["result"]
