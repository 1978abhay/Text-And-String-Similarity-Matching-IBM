from typing import Callable, List
import nltk

from LevenshteinSimscore import sim_score
from checkingifsynonym import is_synonym

nltk.download("stopwords")
stop_words = set(nltk.corpus.stopwords.words("english"))


def process_string(text: str) -> List[str]:
    words = "".join([letter for letter in text if letter.isalpha() or letter == " "])
    return [word for word in words.split(" ") if word.lower() not in stop_words and word != ""]


# Should function as list comprehension version below,
# but will test to see which is more performant.
def longMongeElkan(m: int, text_a: str, text_b: str, sim_func: Callable[[str, str], int]) -> float:
    total = 0
    array_a = process_string(text_a)
    array_b = process_string(text_b)
    for a in array_a:
        max_similarity = float("-inf")
        for b in array_b:
            similarity = sim_func(a, b)

            if similarity > max_similarity:
                max_similarity = similarity
        total += max_similarity ** m

    return (total / len(array_a)) ** (1 / m)


def synonym_monge_elkan(text_a: str, text_b: str) -> float:
    return longMongeElkan(1.5, text_a, text_b, is_synonym)


def levenshtein_monge_elkan(text_a: str, text_b: str) -> float:
    return longMongeElkan(0.7, text_a, text_b, sim_score)


def simMongeElkan(m: int, text_a: str, text_b: str, sim_func: Callable[[str, str], int]) -> float:
    array_b = text_b.split(" ")
    array_a = text_a.split(" ")
    return (sum([max([sim_func(a, b) for b in array_b]) ** m for a in array_a]) / len(array_a)) ** (1 / m)


def quadSimilarityME(text_a: str, text_b: str, sim_func: Callable[[str, str], int]) -> float:
    return simMongeElkan(2, text_a, text_b, sim_func)
