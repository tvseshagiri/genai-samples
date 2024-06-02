from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI


flowchart_url = "https://www.slideteam.net/media/catalog/product/cache/1280x720/p/a/payment_process_via_application_flow_chart_slide01.jpg"


llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")

message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "Examine the image very carefully and explain what is it in there",
        },  # You can optionally provide text parts
        {"type": "image_url", "image_url": flowchart_url},
    ]
)
response = llm.invoke([message])
print(response.content)
