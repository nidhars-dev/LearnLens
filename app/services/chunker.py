from pathlib import Path

from ..models.document import Document
from ..models.chunk import Chunk

class Chunker:

    """
    Chunking service.

    Converts Document objects into smaller Chunk objects
    for embedding and retrieval.

    Supports configurable chunk size and overlap.

    Chunks never cross page boundaries.
    """

    def chunk(
        self,
        document: Document, 
        chunk_size: int = 200, 
        overlap: int = 50
    ) -> list[Chunk]: 
        
        chunks = []
        chunk_counter = 1
        filename = Path(document.filename).stem
        for page in document.pages:

            words = page.text.split()

            start = 0;

            while start < len(words):
                chunk_list = words[start : start + chunk_size]
                chunk_text = " ".join(chunk_list)
    
                chunk = Chunk(
                    chunk_id = f"{filename}_"f"page_{page.page_number}_"f"chunk_{chunk_counter}",
                    text = chunk_text,
                    page_number = page.page_number,
                    source_file = document.filename
                )
                chunks.append(chunk)
                chunk_counter += 1

                start += (chunk_size - overlap)
        
        return chunks

            


    
    
