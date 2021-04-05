from typing import List
import subprocess
import os
from random import randint


from .quote_model import Quote
from .ingestor_interface import IngestorInterface


class PDFIngestor(IngestorInterface):

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        if not cls.can_ingest(path):
            raise ValueError(f'Unable to parse {path}. Allowed file types: {cls.allowed_extensions}.')
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
