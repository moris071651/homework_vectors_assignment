import pytest

from src import load_model, find_common_meaning

@pytest.mark.parametrize('base_word, related_word, target_word, expected', [
    ('horse', 'rider', 'car', 'driver'),
    ('raven', 'bird', 'dog', 'animal'),
    ('free', 'democracy', 'slavery', 'oppression'),
])
def test_find_common_meaning(base_word, related_word, target_word, expected):
    assert find_common_meaning(load_model(), base_word, related_word, target_word) == expected
