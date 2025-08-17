import openai
import os

api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key = api_key)
print(client)

