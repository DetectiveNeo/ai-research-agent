import json


def write_file(content: str):
    with open("json_generated/simple_agent_json.txt" , "w") as file:
        json.dump(content, file, indent= 4)

    print('File is Written')

    return "File is written !"

def finish(content: str):
    return exit(0)

def retrieve_documents(content: str):
    ...


