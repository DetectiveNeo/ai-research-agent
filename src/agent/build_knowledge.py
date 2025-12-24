import re

with open("data/raw/entropy_knowledge_base.txt", "r") as file:
    text = file.read()

print(type(text))

# sentences = [s.]

sentences = re.split(r'\.\s*', text)

# for sentence in sentences:
#     print(sentence)

vectors = []

for chunk in sentences:
    vector = embed(chunk)
    vectors.append(vector)





