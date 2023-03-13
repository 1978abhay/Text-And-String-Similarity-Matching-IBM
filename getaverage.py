
from cosine import get_cosine, text_to_vector
import mongeElkanTest 
import mongeElkan as me
import checkingifsynonym as checkSyn
from jaccard import jaccard_index
X = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible."
Y = "Bees are flying insects closely related to wasps and ants, known for their role in pollination and, in the case of the best-known bee species, the western honey bee, for producinghoney. Bees are a monophyletic lineage within the superfamily Apoidea. They are presently considered a clade, called Anthophila. There are over 16,000 known species of bees in seven recognized biological families. Some species – including honey bees, bumblebees, and stingless bees – live socially in colonies while some species – including mason bees, carpenter bees, leafcutter bees, and sweat bees – are solitary."
vector1 = text_to_vector(X)
vector2 = text_to_vector(Y)
cosine = get_cosine(vector1, vector2)
jaccard =(jaccard_index(X,Y))
cosineVar = round(cosine,3)
mongeElkan1 = me.longMongeElkan(1, X, Y, lambda a,b: int(checkSyn.anotherWord(a,b)))
mongeElkan2 = me.quadSimilarityME(X, Y, lambda a,b: int(checkSyn.anotherWord(a,b)))
average = jaccard + cosineVar + mongeElkan1 + mongeElkan2
average = average/4
print(average)
