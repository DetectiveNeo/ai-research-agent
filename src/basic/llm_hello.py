import subprocess

OLLAMA_PATH = r"C:/Users/meghw/AppData/Local/Programs/Ollama/ollama.exe"

def ask_ollama(promt: str):
    result = subprocess.run(
        [OLLAMA_PATH, "run", "llama3.2"],
        input= promt.encode(),
        stdout= subprocess.PIPE
    )
    print(result.stdout.decode())

if __name__ == "__main__":
    ask_ollama(("Explain what an LLM in simple words."))