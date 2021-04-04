from abc import ABC, abstractmethod
from typing import List

from .quote_model import Quote


class IngestorInterface(ABC):

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, pat: str) -> bool:
        pass

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Quote]:
        pass
