from app.services.vector_store import VectorStore
from app.services.embedder import Embedder

embedder = Embedder()
store = VectorStore("learnlens")

query = "What is the objective of CTF?"

query_embedding = embedder.embed_query(query)

results = store.search(
    query_embedding=query_embedding,
    top_k=3
)

print(results)