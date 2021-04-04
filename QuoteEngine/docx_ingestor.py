from typing import List

from .quote_model import Quote
from .ingestor_interface import IngestorInterface


class DocxIngestor(IngestorInterface):

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        pass
