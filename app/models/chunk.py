from dataclasses import dataclass

@dataclass
class Chunk:
    chunk_id: str
    text: str
    page_number: int
    source_file: str