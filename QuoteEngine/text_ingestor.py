from typing import List

from .quote_model import Quote
from .ingestor_interface import IngestorInterface


class TextIngestor(IngestorInterface):

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        if not cls.can_ingest(path):
            raise ValueError(f'Unable to parse {path}. Allowed file types: {cls.allowed_extensions}.')
        quotes = []
        with open(path) as f:
            for line in f.readlines():
                quote_parts = [part.strip() for part in line.split('-')]
                if len(quote_parts) == 2:
                    quote = Quote(quote_parts[0], quote_parts[1])
                    quotes.append(quote)
        return quotes
