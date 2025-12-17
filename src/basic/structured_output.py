import json
from openai import OpenAI
from src.config import OPENAI_API_KEY

client = OpenAI(api_key= OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are an AI research assistant.
You must respond only in JSON format.
Do not include markdown, code fences, or no explanations

The output should be striclty in this Expected JSON Format :
{
    'heading' : 'string',
    'content' : ['string1', 'string2', 'string3']
}

Rules:
- Use Simple, clear language
- Exactly 3 items in "content"
- No Additional Keys

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

parsed_output = json.loads(raw_output)

print('------------------------------------------------------------------')

print('Parsed_output Output')
print(f"Heading : {parsed_output['heading']}")
print('Key Points')
for i, point in enumerate(parsed_output['content']):
    print(f'Point Number {i} : {point}')

with open("json_generated/structured_ouput_py", "w") as file:
    json.dump(parsed_output, file, indent= 4)

