from app.services.vector_store import VectorStore
from app.services.embedder import Embedder
from app.services.retriever import Retriever

embedder = Embedder()
store = VectorStore("learnlens")
retriever = Retriever(embedder, store)

query = "What is the objective of CTF?"

results = retriever.retrieve(query, top_k=3)

print(results)