from utils import load_urls_data

from langchain.text_splitter import CharacterTextSplitter

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.vectorstores.chroma import Chroma

from dotenv import load_dotenv
from langchain_openai.llms import OpenAI
from langchain_openai import OpenAIEmbeddings


import os

load_dotenv()


embeddings = OpenAIEmbeddings()


docsearch = None
if not os.path.exists("./chroma_db"):
    docs = load_urls_data("inputs/urls.csv")

    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=1000,
        chunk_overlap=0,
        length_function=len,
        # is_separator_regex=False,
    )

    texts = text_splitter.split_documents(docs)

    docsearch = Chroma.from_documents(
        texts, embeddings, persist_directory="./chroma_db"
    )
else:
    print("I am loading embeddings from local disk")
    docsearch = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=docsearch.as_retriever(),
)


qry = ""

while True:
    try:
        qry = input("Enter your query: ")
        if qry == "exit":
            exit(0)
        else:
            print("System: %s \n" % qa.invoke(qry)["result"])
    except Exception as e:
        if e.code == 429:
            pass
        else:
            print(e.error)
