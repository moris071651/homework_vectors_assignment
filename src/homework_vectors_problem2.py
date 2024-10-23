from homework_vectors_problem1 import calculate_similarity, Model, Word

def find_common_meaning(model: Model, base_word: Word, related_word: Word, target_word: Word) -> Word:
    common_word = None
    max_sim = float('-inf')

    vec_base = model[base_word]
    vec_related = model[related_word]
    vec_target = model[target_word]

    diff_vec = [x - y + z for x, y, z in zip(vec_related, vec_base, vec_target)]

    for word, vec in model.items():
        if word in [base_word, related_word, target_word]:
            continue

        sim = calculate_similarity(model, vec, diff_vec)
        if sim > max_sim:
            max_sim = sim
            common_word = word

    return common_word
