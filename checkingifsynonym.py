from nltk.corpus import wordnet as wn


# This returns True if two words have the same meaning, otherwise false
def is_synonym(a: str, b: str) -> bool:
    if a == b:
        return True

    synonym_sets = wn.synsets(a)
    for synonym in wn.synsets(a):
        for lemma in synonym.lemma_names():
            if b == lemma:
                return True
    return False
