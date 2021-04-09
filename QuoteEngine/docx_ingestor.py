from typing import List
import docx

from .quote_model import Quote
from .ingestor_interface import IngestorInterface


class DocxIngestor(IngestorInterface):
    """Class for extracting quotes from docx files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Extract quotes from a docx file.

        :param path: Path to a file.
        :return: List of Quote objects.
        """
        cls.file_type_guard(path)
        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            quote_parts = [part.strip() for part in para.text.split('-')]
            if len(quote_parts) == 2:
                quote = Quote(quote_parts[0], quote_parts[1])
                quotes.append(quote)
        return quotes
