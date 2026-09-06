from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model=SentenceTransformer("all-MiniLM-L6-v2")

texts=[
    "User input is directly inserted into a SQL query.",
    "User input is safely parameterized in a SQL query.",
    "The weather is sunny today"
]
embeddings = model.encode(texts)

similarity=cosine_similarity(embeddings)
print(similarity)