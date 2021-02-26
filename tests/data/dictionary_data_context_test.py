from src.data.dictionary_data_context import DictionaryDataContext
from src.game_token.game_token import GameToken


def test_get_existing_entity(testing_data_context: DictionaryDataContext):
    test_kind = "game_tokens"
    test_key = "key_1"
    entity = testing_data_context.get(test_kind, test_key)

    assert entity is not None
    assert type(entity) is GameToken
    assert entity.game_token_id == test_key


def test_get_non_existent_entity(testing_data_context: DictionaryDataContext):
    test_kind = "game_tokens"
    test_key = "non_existent_key"
    entity = testing_data_context.get(test_kind, test_key)

    assert entity is None


def test_get_all(testing_data_context: DictionaryDataContext):
    test_kind = "game_tokens"
    entities = testing_data_context.get_all(test_kind)

    assert entities is not None
    assert type(entities) is list
    assert len(entities) > 0


def test_create(testing_data_context: DictionaryDataContext, game_token_without_id: GameToken):
    test_kind = "game_tokens"

    entity = testing_data_context.create(test_kind, game_token_without_id)

    assert entity is not None
    assert type(entity) is GameToken
    assert entity.game_token_id is not None
    assert testing_data_context.get(test_kind, entity.game_token_id)


def test_update_existing_entity(testing_data_context: DictionaryDataContext):
    pass


def test_update_non_existent_entity(testing_data_context: DictionaryDataContext):
    pass


def test_delete(testing_data_context: DictionaryDataContext):
    pass
