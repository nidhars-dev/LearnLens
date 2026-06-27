from app.services.embedder import Embedder
from app.services.vector_store import VectorStore


class Retriever:
    """
    Retrieval service.

    Responsible for:
    1. Converting a user query into an embedding.
    2. Searching the vector database.
    3. Returning clean retrieval results.
    """
    def __init__(
            self, 
            embedder: Embedder, 
            vector_store: VectorStore):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(
            self,
            query: str,
            top_k: int = 3
    ) -> list[dict]:
        """
        Retrieve the top-k most similar documents to the given query.

        Args:
            query: The search query.
            top_k: The number of top results to return.

        Returns:
            A list of dictionaries containing the retrieved documents.
        """
        query_embedding = self.embedder.embed_query(query)
        results = self.vector_store.search(query_embedding, top_k)
        
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        retrieved_chunks = []

        for i in range(len(documents)):
            retrieved_chunks.append({
                "document": documents[i],
                "page_number": metadatas[i]["page_number"],
                "source_file": metadatas[i]["source_file"],
                "distance": distances[i]
            })

        return retrieved_chunks