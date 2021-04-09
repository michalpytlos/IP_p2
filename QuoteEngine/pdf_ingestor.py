from typing import List
import subprocess
import os
from random import randint


from .quote_model import Quote
from .ingestor_interface import IngestorInterface


class PDFIngestor(IngestorInterface):
    """Class for extracting quotes from pdf files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Extract quotes from a pdf file.

        :param path: Path to a file.
        :return: List of Quote objects.
        """
        cls.file_type_guard(path)
        quotes = []
        tmp = f'pdftotext_tmp_{randint(0, 10000)}.txt'
        subprocess.call(['pdftotext', path, tmp])
        with open(tmp) as f:
            for line in f.readlines():
                quote_parts = [part.strip() for part in line.split('-')]
                if len(quote_parts) == 2:
                    quote = Quote(quote_parts[0], quote_parts[1])
                    quotes.append(quote)
        os.remove(tmp)
        return quotes
