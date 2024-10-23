import json
import functools

from . import homework_vectors_problem1
from . import homework_vectors_problem2


@functools.cache
def load_model(path: str = 'word_vectors.json'):
    with open(path) as f:
        model = json.load(f)
    
    return model


def calculate_similarity(model, base_word, target_word):
    return homework_vectors_problem1.calculate_similarity(model, base_word, target_word)


def find_most_similar_to_given(model, given_word, target_words):
    return homework_vectors_problem1.find_most_similar_to_given(model, given_word, target_words)


def doesnt_match(model, given_words):
    return homework_vectors_problem1.doesnt_match(model, given_words)


def find_common_meaning(model, base_word, related_word, target_word):
    return homework_vectors_problem2.find_common_meaning(model, base_word, related_word, target_word)
