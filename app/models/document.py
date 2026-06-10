from dataclasses import dataclass
from .page import Page

@dataclass
class Document:
    filename: str
    total_pages: int
    pages: list[Page]