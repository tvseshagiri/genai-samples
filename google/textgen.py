import google.generativeai as genai

model = genai.GenerativeModel("gemini-pro")

prompt = """
What is the capital city of Papua New Guinea?
"""

response = model.generate_content(prompt)

print(response.text)
