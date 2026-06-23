from app.services.embedder import Embedder
from app.services.pdf_extractor import PDFExtractor
from app.services.chunker import Chunker

extractor = PDFExtractor()
document = extractor.extract("data/sample.pdf")

chunker = Chunker()
chunks = chunker.chunk(document)

embedder = Embedder()
embedded_chunks = embedder.embed(chunks)

print(f"Total chunks: {len(chunks)}")
print(f"Total embedded chunks: {len(embedded_chunks)}")

print(f"First embedded chunk text: {embedded_chunks[0].chunk.text}")
print(f"First embedded chunk page number: {embedded_chunks[0].chunk.page_number}")
print(f"First embedded chunk source file: {embedded_chunks[0].chunk.source_file}")
print(f"Embedding dimensions: {len(embedded_chunks[0].embedding)}")