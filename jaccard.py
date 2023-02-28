from typing import List


def jaccard_index(a: str, b: str) -> float:
    """Calculates the jaccard index of two strings.

    :return: A floating point number between in the range [0, 1].
    """

    # TODO: Figure out ideal w for shingling

    if a is None or b is None:
        raise ValueError("Recieved None argument to jaccard index.")

    def shingle(s: str, w=2) -> List[str]:
        """Return the w-shingle of the string s.

        :param str s: The string to shingle
        :param int w: The size of the w-shingle, assumed to be >= 1. Default is 2.
        :return: The shingled string
        """
        if w < 1 or s is None:
            raise ValueError("Invalid argument")

        words = tuple(s.split())  # Use tuples because lists cannot be used in sets
        return [words[i : i + w] for i in range(len(words) - w + 1)]

    a_words = set(shingle(a))
    b_words = set(shingle(b))
    return len(a_words.intersection(b_words)) / len(a_words.union(b_words))
