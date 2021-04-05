from typing import List

from .quote_model import Quote
from .ingestor_interface import IngestorInterface
from .csv_ingestor import CSVIngestor
from .pdf_ingestor import PDFIngestor
from .text_ingestor import TextIngestor
from .docx_ingestor import DocxIngestor


class Ingestor(IngestorInterface):

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        checked_extensions = []
        for ingestor in [CSVIngestor, TextIngestor, DocxIngestor, PDFIngestor]:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
            checked_extensions.extend(ingestor.allowed_extensions)
        raise ValueError(f'Unable to parse {path}. Allowed file types: {checked_extensions}')
