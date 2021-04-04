from typing import List

from .quote_model import Quote
from .ingestor_interface import IngestorInterface


class CSVIngestor(IngestorInterface):

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        pass
