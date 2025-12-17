import json
from openai import OpenAI
from src.config import OPENAI_API_KEY

client = OpenAI(api_key= OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are an AI research assistant.
You must respond only in JSON format.
No markdowm
No code fences
No explanation

Expected JSON Format :
{
    'heading' : 'string',
    'content' : ['string1', 'string2', 'string3']
}

"""

USER_PROMPT = """
What is a bottle ?
"""

responses = client.responses.create(
    model= 'gpt-4.1-mini',
    output= [
        {
            'role' : 'system',
            'content' : SYSTEM_PROMPT
        },
        {
            'role' : 'user',
            'content' : USER_PROMPT
        }
    ]
)

print(responses.output_text)

