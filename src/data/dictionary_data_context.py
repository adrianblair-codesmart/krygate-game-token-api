from abc import ABC, abstractmethod
import uuid

from src.data.abstract_data_context import AbstractDataContext
from src.game_token.game_token import GameToken


class DictionaryDataContext(AbstractDataContext):
    def __init__(self, db_client: dict[str, list[GameToken]]):
        super().__init__(db_client)

    def get(self, kind: str, entity_id: str) -> GameToken:
        return self.find(kind, entity_id)

    def get_all(self, kind: str) -> list[GameToken]:
        return self._db_client[kind]

    def create(self, kind: str, entity: GameToken) -> GameToken:
        entity.game_token_id = str(uuid.uuid4())
        entities = self._db_client[kind]
        entities.append(entity)
        return entity

    def update(self, kind: str, entity: GameToken) -> GameToken:
        entities = self._db_client[kind]

        i = self.index(kind, entity.game_token_id)

        if i > 0:
            entities[i] = entity
            return entity

    def delete(self, kind: str, entity_id: str):
        entities = self._db_client[kind]
        entities.remove(entity_id)

    def index(self, kind: str, entity_id: str):
        entities = self._db_client[kind]

        for i, entity in enumerate(entities):
            if entity.game_token_id == entity_id:
                return i

        return -1

    def find(self, kind: str, entity_id: str):
        entities = self._db_client[kind]
        i = self.index(kind, entity_id)

        if i >= 0:
            return entities[i]

