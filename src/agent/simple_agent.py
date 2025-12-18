"""
Docstring for src.agent.simple_agent

An agent loop is a program where LLM plans an action, your code executes it, and then LLM observed the result and decides what to do next.

An agent does the following thingh necessarily
1) Think/Plan : LLM plans the action
2) Act : your code executes something
3) Observe/Stop : agent decides it is done

Simple AI agent AI decides what to do next and the Python code does it.

"""


from openai import OpenAI
import json
from src.config import OPENAI_API_KEY

client = OpenAI(api_key= OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are a simple Python AI Agent.

Your job is to decide the next action needed to complete task.

You must respond ONLY with valid JSON.

{
    "thought" : string,
    "action" : "write" or "finish",
    "content" : string
}

Rules :
- Choose exactly one action at a time "write" or "finish"
- If you recieve confirmation that the Task is completed then you mush choose action "finish"
- Content should be in simple plain words. (Maximum Words allowed : 10)
- No Markdown no explanations
"""

TASK = "What is a bottle ? save it in a file"


response = client.responses.create(
    model= "gpt-4.1-mini",
    input= [
        {
            "role" : "system",
            "content" : SYSTEM_PROMPT
        },
        {
            "role" : "user",
            "content" : TASK
        }
    ]
)

raw_output = response.output_text

print(raw_output)

parsed_output = json.loads(raw_output)

# print(parsed_output)
# print(type(parsed_output))
# print(parsed_output['thought'])

print('-----------------------------------------------')

if parsed_output['action'] not in ['write', 'finish']:
    raise ValueError('Invalid action returned by Agent')

if parsed_output['action'] == 'write' :
    with open("json_generated/simple_agent_json.txt" , "w") as file:
        json.dump(parsed_output['content'], file, indent= 4)

    print('File written : simple_agent_json')

    feedback = "File is written"

    response = client.responses.create(
        model= 'gpt-4.1-mini',
        input= [
            {
                "role" : "system",
                "content" : SYSTEM_PROMPT 
            },
            {
                "role" : "user",
                "content" : feedback
            }
        ]
    )

    final_raw = response.output_text
    final_decision = json.loads(final_raw)

    print(f"Final Action : {final_decision['action']}")

    if final_decision['action'] == 'finish':
        print('Task Done Successfully')



