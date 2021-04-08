from typing import List
import pandas

from .quote_model import Quote
from .ingestor_interface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """Class for extracting quotes from csv files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Extract quotes from a csv file.

        :param path: Path to a file.
        :return: List of Quote objects.
        """
        if not cls.can_ingest(path):
            raise ValueError(f'Unable to parse {path}. Allowed file types: {cls.allowed_extensions}.')
        quotes = []
        df = pandas.read_csv(path)
        for index, row in df.iterrows():
            quote = Quote(row['body'], row['author'])
            quotes.append(quote)
        return quotes
