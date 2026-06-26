from ollama import embed

from ..models.chunk import Chunk
from ..models.embedded_chunk import EmbeddedChunk

class Embedder:

    def embed(
        self, 
        chunks: list[Chunk]
    ) -> list[EmbeddedChunk]:
        
        text = [chunk.text for chunk in chunks]
        response = embed(
            model = 'nomic-embed-text', 
            input = text)

        embedded_chunks = []
        for chunk, embedding in zip(chunks, response.embeddings):
            embedded_chunk = EmbeddedChunk(
                chunk = chunk,
                embedding = embedding
            )
            embedded_chunks.append(embedded_chunk)

        return embedded_chunks
    
    def embed_query(
            self,
            text : str
        ) -> list[float]:
        response = embed(
            model = 'nomic-embed-text', 
            input = text)
        return response.embeddings[0]
    