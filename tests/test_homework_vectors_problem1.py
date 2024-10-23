import pytest

from src import load_model
from src import calculate_similarity
from src import find_most_similar_to_given
from src import doesnt_match

@pytest.mark.parametrize('base_word, target_word, expected', [
    ('hello', 'robot', 0.3609110823506898),
    ('mountain', 'rabbit', 0.3611828985366266),
    ('box', 'heart', 0.4429130340830195),
])
def test_calculate_similarity(base_word, target_word, expected):
    assert calculate_similarity(load_model(), base_word, target_word) == expected


@pytest.mark.parametrize('given_word, target_words, expected', [
    ('school', ['building', 'student', 'road'], 'student'),
    ('apple', ['fruit', 'house', 'pen'], 'fruit'),
    ('animal', ['horse', 'board', 'book', 'key'], 'horse'),
])
def test_find_most_similar_to_given(given_word, target_words, expected):
    assert find_most_similar_to_given(load_model(), given_word, target_words) == expected


@pytest.mark.parametrize('given_words, expected', [
    (['apple', 'pear', 'banana', 'car'], 'car'),
    (['city', 'computer', 'road', 'house'], 'computer'),
    (['gamer', 'raven', 'computer', 'game'], 'raven'),
])
def test_doesnt_match(given_words, expected):
    assert doesnt_match(load_model(), given_words) == expected
