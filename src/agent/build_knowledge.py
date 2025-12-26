import re
from openai import OpenAI
import faiss
import numpy as np

from src.config import OPENAI_API_KEY

client = OpenAI(api_key= OPENAI_API_KEY)

with open("data/raw/entropy_knowledge_base.txt", "r") as file:
    text = file.read()

# sentences = [s.]

sentences = re.split(r'\.\s*', text)

# for sentence in sentences:
#     print(sentence)

def embed(text, model= "text-embedding-3-small"):
    response = client.embeddings.create(
        model= model,
        input= text
    )

    vector = response.data[0].embedding

    return vector

vectors = []

for chunk in sentences:
    if len(chunk) < 10 :
        continue
    vector = embed(chunk)
    vectors.append(vector)

    break

vector_array = np.array(vectors).astype("float32")

print(len(vectors))
print(len(vectors[0]))





