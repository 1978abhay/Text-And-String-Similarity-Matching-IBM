from typing import Callable


# Should function as list comprehension version below,
# but will test to see which is more performant.
def longMongeElkan(m: int, text_a: str, text_b: str, sim_func: Callable[[str, str], int]) -> float:
    total = 0
    array_a = text_a.split(" ")
    array_b = text_b.split(" ")
    for a in array_a:
        max_similarity = float("-inf")
        for b in array_b:
            similarity = sim_func(a, b)
            if similarity > max_similarity:
                max_similarity = similarity
        total += max_similarity ** m

    return (total / len(array_a)) ** (1 / m)


def simMongeElkan(m: int, text_a: str, text_b: str, sim_func: Callable[[str, str], int]) -> float:
    array_b = text_b.split(" ")
    array_a = text_a.split(" ")
    return (sum([max([sim_func(a, b) for b in array_b]) ** m for a in array_a]) / len(array_a)) ** (1 / m)


def quadSimilarityME(text_a: str, text_b: str, sim_func: Callable[[str, str], int]) -> float:
    return simMongeElkan(2, text_a, text_b, sim_func)
