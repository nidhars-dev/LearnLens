from dataclasses import dataclass
from typing import List

@dataclass
class Page:
    page_number: int
    text: str