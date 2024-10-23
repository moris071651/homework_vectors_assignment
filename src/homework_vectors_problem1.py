from math import sqrt
from typing import Dict, List

Vec = List[float]
Word = str | None
Model = Dict[Word, Vec]

def calculate_similarity(model: Model, base_word: Word | Vec, target_word: Word | Vec) -> float:
    if base_word is None or target_word is None:
        raise ValueError

    vec1 = base_word if isinstance(base_word, list) else model[base_word]
    vec2 = target_word if isinstance(target_word, list) else model[target_word]

    a = sum([x * y for x, y in zip(vec1, vec2)])

    mag = lambda vec: sqrt(sum([x * x for x in vec]))
    b = mag(vec1) * mag(vec2)

    return a / b if b != 0 else 0.0


def find_most_similar_to_given(model: Model, given_word: Word, target_words: List[Word]) -> Word:
    match_word = None
    max_sim = float('-inf')

    for word in target_words:
        sim = calculate_similarity(model, given_word, word)
        if sim > max_sim:
            max_sim = sim
            match_word = word

    return match_word


def doesnt_match(model: Model, given_words: List[Word]) -> Word:
    odd_word = None
    min_sim = float('inf')

    avg = lambda x: sum(x) / len(x)

    for word in given_words:
        sim = avg([
            calculate_similarity(model, word, w)
            for w in given_words if w != word
        ])

        if sim < min_sim:
            min_sim = sim
            odd_word = word

    return odd_word

