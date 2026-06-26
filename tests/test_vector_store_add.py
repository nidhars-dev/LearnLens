from app.services.pdf_extractor import PDFExtractor
from app.services.chunker import Chunker
from app.services.embedder import Embedder
from app.services.vector_store import VectorStore


# Create service objects
extractor = PDFExtractor()
chunker = Chunker()
embedder = Embedder()
vector_store = VectorStore("learnlens")


# Extract PDF
document = extractor.extract("data/sample.pdf")

# Create chunks
chunks = chunker.chunk(document)

# Create embeddings
embedded_chunks = embedder.embed(chunks)

# Store embeddings
vector_store.add(embedded_chunks)

print(f"Stored {len(embedded_chunks)} embedded chunks successfully.")