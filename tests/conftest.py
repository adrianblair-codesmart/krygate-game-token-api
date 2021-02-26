import pytest

from src.data.dictionary_data_context import DictionaryDataContext
from src.game_token.game_token import GameToken


@pytest.fixture
def game_token_without_id():
    return GameToken(**{
        "game_token_name": "this is a new token.",
        "game_token_key": "this is a new token key.",
        "allowed_domains": ["bits-and-bobs.com"]
    })


@pytest.fixture
def game_token_with_id():
    return GameToken(**{
        "game_token_id": "the id for this token.",
        "game_token_name": "this is a new token.",
        "game_token_key": "this is a new token key.",
        "allowed_domains": ["bits-and-bobs.com"]
    })


@pytest.fixture
def testing_data_context():
    entity_1 = GameToken(**{
        "game_token_id": "key_1",
        "game_token_name": "this is a new token.",
        "game_token_key": "this is a new token key.",
        "allowed_domains": ["bits-and-bobs.com"]
    })

    entity_dict = dict([("game_tokens", [entity_1])])

    return DictionaryDataContext(entity_dict)
