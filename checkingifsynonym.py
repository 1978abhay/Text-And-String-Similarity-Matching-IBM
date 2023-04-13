from nltk.corpus import wordnet as wn


# This returns True if two words have the same meaning, otherwise false
def is_synonym(a: str, b: str) -> bool:
    if a == b:
        return True
    for synonym in wn.synsets(a):
        if b in synonym.lemma_names():
            return True

    return False
