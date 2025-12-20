"""
Docstring for src.agent.simple_agent

An agent loop is a program where LLM plans an tool, your code executes it, and then LLM observed the result and decides what to do next.

An agent does the following thingh necessarily
1) Think/Plan : LLM plans the tool
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

Your job is to decide the next tool needed to complete task.

You must respond ONLY with valid JSON.

{
    "thought" : string,
    "tool" : "write_file" or "finish",
    "tool_input" : {
            "content" : string
        }
}

Rules :
- Choose exactly one tool at a time "write_file" or "finish"
- If you recieve confirmation that the Task is completed then you mush choose tool "finish"
- Content should be in simple plain words. (Maximum Words allowed : 10)
- No Markdown no explanations
"""

def write_file(content: str) -> None:
        """
        Docstring for write_file

        Writes content to a file and returns a status message.
        
        :param content: Description
        :type content: str
        """
        with open("json_generated/simple_agent_json.txt" , "w") as file:
            json.dump(content, file, indent= 4)

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

        print(f"Final tool : {final_decision['tool']}")

        if final_decision['tool'] == 'finish':
            print('Task Done Successfully')



TOOLS = {
    "write_file" : write_file,
    # "finish" : finish
}


TASK = "What is a bottle ? save it in a file"


if __name__ == "__main__":
     
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


    TOOLS[parsed_output['tool'](parsed_output['tool_input']['content'])]

