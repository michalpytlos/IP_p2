from abc import ABC, abstractmethod
from typing import List

from .quote_model import Quote


class IngestorInterface(ABC):

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.split('.')[-1] in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Quote]:
        pass
