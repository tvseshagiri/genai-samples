import csv
from langchain_community.document_loaders.web_base import WebBaseLoader
import nest_asyncio


def load_urls(csv_file):
    urls_list = []
    with open(csv_file, "r") as f:
        csv.reader(f)
        for row in csv.reader(f):
            urls_list.append(row[0])
    return urls_list


def load_urls_data(urls_csv):
    urls = load_urls(urls_csv)
    req_headers = {
        "User-Agent": "Chrome",
    }

    nest_asyncio.apply()
    loader = WebBaseLoader(urls, header_template=req_headers)
    docs = loader.load()
    # print(docs)
    return docs
