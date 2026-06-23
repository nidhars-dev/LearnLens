from dataclasses import dataclass
from .chunk import Chunk


@dataclass
class EmbeddedChunk:
    """
    Stores a chunk together with its vector embedding.

    The embedding represents the semantic meaning
    of the chunk in a 768-dimensional vector space.
    """

    chunk: Chunk
    embedding : list[float]
