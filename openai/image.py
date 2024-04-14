from openai import OpenAI

openai = OpenAI()

prompt = "An early morning long drive in Ferrari car with clear visibility of Ferrari logo and sun"
model = "dall-e-2"

# Generate an image based on the prompt
response = openai.images.generate(prompt=prompt, model=model)

# Prints response containing a URL link to image
print(response)
