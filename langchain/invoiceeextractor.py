from unstructured.partition.pdf import partition_pdf, PartitionStrategy
from langchain_community.document_loaders.unstructured import UnstructuredFileLoader
from pydantic import BaseModel
import os


def extract_invoice(pdf_file):
    loader = UnstructuredFileLoader(file_path=pdf_file, mode="elements")
    docs = loader.load()

    # append all docs.page_content to a single string
    text = ""
    for doc in docs:
        text += doc.page_content

    from langchain.chains import (
        create_extraction_chain,
        create_extraction_chain_pydantic,
    )
    from dotenv import load_dotenv
    from langchain_openai.chat_models import ChatOpenAI

    load_dotenv()

    OrderItemSchema = {
        "properties": {
            "Description": {"type": "string"},
            "Unit Price": {"type": "string"},
            "Qty": {"type": "string"},
            "Net Amount": {"type": "string"},
            "Tax Rate": {"type": "string"},
            "Tax Type": {"type": "string"},
            "Tax Amount": {"type": "string"},
            "Total Amount": {"type": "string"},
        }
    }

    schema = {
        "properties": {
            "Billing Address": {"type": "string"},
            "TOTAL": {"type": "array", "items": {"TOTAL": {"type": "string"}}},
            "PAN No": {"type": "string"},
            "Order Number": {"type": "string"},
            "Invoice Number": {"type": "string"},
            "Invoice Date": {"type": "string"},
            "extra_info": {"type": "string"},
            "description": {"type": "string"},
            "GST Registration No": {"type": "string"},
            "orderItems": {
                "type": "array",
                "items": {
                    "Description": {"type": "string"},
                    "Unit Price": {"type": "string"},
                    "Qty": {"type": "string"},
                    "Net Amount": {"type": "string"},
                    "Tax Rate": {"type": "string"},
                    "Tax Type": {"type": "string"},
                    "Tax Amount": {"type": "string"},
                    "Total Amount": {"type": "string"},
                },
            },
            "Amount in Words": {"type": "string"},
        },
        "required": ["Order Number", "TOTAL", "Billing Address", "GST Registration No"],
    }
    llm = ChatOpenAI(temperature=0)
    chain = create_extraction_chain(schema=schema, llm=llm)
    print(chain.invoke(text)["text"])


pdf_file = "../inputs/amazon-invoice.pdf"

extract_invoice(pdf_file=pdf_file)
