from typing import List
import itertools

def jaccard_index(a: str, b: str) -> float:
    """Calculates the jaccard index of two strings.

    :return: A floating point number between in the range [0, 1].
    """

    if a is None or b is None:
        raise ValueError("Recieved None argument to jaccard index.")

    a = set(a)
    b = set(b)
    return len(a.intersection(b)) / len(a.union(b))
X = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible."
Y = "Bees are flying insects closely related to wasps and ants, known for their role in pollination and, in the case of the best-known bee species, the western honey bee, for producinghoney. Bees are a monophyletic lineage within the superfamily Apoidea. They are presently considered a clade, called Anthophila. There are over 16,000 known species of bees in seven recognized biological families. Some species – including honey bees, bumblebees, and stingless bees – live socially in colonies while some species – including mason bees, carpenter bees, leafcutter bees, and sweat bees – are solitary."