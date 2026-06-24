from app.services.pdf_extractor import PDFExtractor
from app.services.chunker import Chunker

extractor = PDFExtractor()
document = extractor.extract("data/sample.pdf")

chunker = Chunker()
chunks = chunker.chunk(document)

print(f"Total chunks: {len(chunks)}")

print(f"Chunk ID: {chunks[0].chunk_id}")
print(f"First chunk text: {chunks[0].text}")
print(f"First chunk page number: {chunks[0].page_number}")
print(f"First chunk source file: {chunks[0].source_file}")

print(f"Chunk ID: {chunks[1].chunk_id}")
print(f"First chunk text: {chunks[1].text}")
print(f"First chunk page number: {chunks[1].page_number}")
print(f"First chunk source file: {chunks[1].source_file}")
