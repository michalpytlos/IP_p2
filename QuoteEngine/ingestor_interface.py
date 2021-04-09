from abc import ABC, abstractmethod
from typing import List

from .quote_model import Quote


class IngestorInterface(ABC):
    """Interface for classes capable of extracting quotes from files."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if this class can ingest a given file."""
        return path.split('.')[-1] in cls.allowed_extensions

    @classmethod
    def file_type_guard(cls, path: str):
        if not cls.can_ingest(path):
            allowed_types = ', '.join(cls.allowed_extensions)
            raise ValueError(
                f'Unable to parse {path}. Allowed file types: {allowed_types}.'
            )

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Quote]:
        """Extract quotes from a file.

        :param path: Path to a file.
        :return: List of Quote objects.
        """
        pass
