from abc import ABC, abstractmethod


class AbstractDataContext(ABC):
    def __init__(self, db_client):
        self._db_client = db_client

    @abstractmethod
    def get(self, kind: str, entity_id: str):
        pass

    def get_all(self, kind: str):
        pass

    @abstractmethod
    def create(self, kind: str, entity):
        pass

    @abstractmethod
    def update(self, kind: str, entity):
        pass

    @abstractmethod
    def delete(self, kind: str, entity_id: str):
        pass
