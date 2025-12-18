"""
Docstring for src.agent.simple_agent

An agent loop is a program where LLM plans an action, your code executes it, and then LLM observed the result and decides what to do next.

"""


from openai import OpenAI
import json
from src.config import OPENAI_API_KEY

client = OpenAI(api_key= OPENAI_API_KEY)

user_prompt = "Hi GPT"

response = client.responses.create(
    model= "gpt-4.1-mini",
    input= user_prompt
)

print(response.output_text)


