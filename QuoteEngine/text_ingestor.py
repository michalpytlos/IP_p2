from typing import List

from .quote_model import Quote
from .ingestor_interface import IngestorInterface


class TextIngestor(IngestorInterface):

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        pass
