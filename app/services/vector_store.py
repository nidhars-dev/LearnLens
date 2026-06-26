

from chromadb import PersistentClient

from app.models.embedded_chunk import EmbeddedChunk


class VectorStore:
        """
        Vector storage service.

        Responsible for storing and retrieving
        embedded chunks from ChromaDB.
        """
        def __init__(
            self, 
            collection_name: str
            ):
                self.collection_name = collection_name

                self.client = PersistentClient(path = "vector_db")

                self.collection = self.client.get_or_create_collection(
                    name = self.collection_name
                )
    
        
        def add(
            self,
            embedded_chunks: list[EmbeddedChunk]
        ):
                ids = []
                documents = []
                embeddings = []
                metadatas = []

                for embedded_chunk in embedded_chunks:
                    ids.append(embedded_chunk.chunk.chunk_id)
                    documents.append(embedded_chunk.chunk.text)
                    embeddings.append(embedded_chunk.embedding)
                    metadatas.append({
                        "page_number": embedded_chunk.chunk.page_number,
                        "source_file": embedded_chunk.chunk.source_file
                    })

        
                self.collection.add(
                        ids=ids,
                        documents=documents,
                        embeddings=embeddings,
                        metadatas=metadatas
                )

        def search(
            self,
            query_embedding: list[float],
            top_k: int
        ):
               results = self.collection.query(
                        query_embeddings=[query_embedding],
                        n_results=top_k
                        )
               return results