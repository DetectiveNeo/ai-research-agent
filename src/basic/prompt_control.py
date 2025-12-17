from openai import OpenAI
from src.config import OPENAI_API_KEY

client = OpenAI(api_key= OPENAI_API_KEY)

"""
SYSTEM PROMPT defines the rules of the universe for the model. A Operating Policy , A constiution
Properties : Highest Priority, Cannot be overidden , should be stable across calls.
"""

SYSTEM_PROMT = """
You are an AI research assistant.
Follow these rules strictly.
1. Respond in bullet points only
2. Use Simple Language
3. Do not exceed maximum of 3 points
4. Give me in a JSON format
5. Also give Headings
"""

USER_PROMPT = """
Explain what a bottle is ? 
"""

response = client.responses.create(
    model= "gpt-4.1-mini",
    input= [
        {
            "role" : "system",
            "content" : SYSTEM_PROMT
        },
        {
            "role" : "user",
            "content" : USER_PROMPT
        },
    ]
)

print(response.output_text)

