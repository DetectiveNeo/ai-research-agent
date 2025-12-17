from openai import OpenAI
from src.config import OPENAI_API_KEY

client = OpenAI(api_key= OPENAI_API_KEY)

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain what a bottle is in simple terms."
)

print(response.output_text)


