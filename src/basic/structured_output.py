import json
from openai import OpenAI
from src.config import OPENAI_API_KEY

client = OpenAI(api_key= OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are an AI research assistant.
You must respond only in JSON format.
No markdowm
No code fences
Explanation Should be in Simple words

Expected JSON Format :
{
    'heading' : 'string',
    'content' : ['string1', 'string2', 'string3']
}

"""

USER_PROMPT = """
What is a bottle ?
"""

response = client.responses.create(
    model= 'gpt-4.1-mini',
    input= [
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

raw_output = response.output_text

print(f'Raw Output : {raw_output}')

parsed = json.loads(raw_output)

print('------------------------------------------------------------------')

print('Parsed Output')
print(f"Heading : {parsed['heading']}")
print('Key Points')
for i, point in enumerate(parsed['content']):
    print(f'Point Number {i} : {point}')


