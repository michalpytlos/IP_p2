from typing import List

from .quote_model import Quote
from .ingestor_interface import IngestorInterface


class TextIngestor(IngestorInterface):
    """Class for extracting quotes from plain text files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Extract quotes from a plain text file.

        :param path: Path to a file.
        :return: List of Quote objects.
        """
        cls.file_type_guard(path)
        quotes = []
        with open(path) as f:
            for line in f.readlines():
                quote_parts = [part.strip() for part in line.split('-')]
                if len(quote_parts) == 2:
                    quote = Quote(quote_parts[0], quote_parts[1])
                    quotes.append(quote)
        return quotes
