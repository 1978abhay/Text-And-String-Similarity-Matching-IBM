import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter


def get_cosine(vec1, vec2):
    # similarity = cosθ = A · B / ||A|| ||B||
    # A · B
    intersection = set(vec1).intersection(vec2)                   # Words which appear in both vectors
    numerator = sum([vec1[x] * vec2[x] for x in intersection])    # Numerator is how many times the intersection words appear
    
    # ||A|| ||B||
    sum_vec1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])     # sum of vector1 values squared, vlaue being how often each word appears
    sum_vec2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])     # sum of vector2 values squared
    denominator = math.sqrt(sum_vec1) * math.sqrt(sum_vec2)       # Denominator is the sqaure root of the prodcut of the vector sums 

    if not denominator:                                           # If demoniator value is 0 or null
        return 0.0
    else:
        return float(numerator) / denominator                     # cosine value
        

def text_to_vector(text):                                         # Vector of the words in a text and how often they occur
    stop_words = set(stopwords.words('english'))                  # Removing stopwords 
    words = word_tokenize(text)                                   # Finds all the words in the text and returns them as a list of strings
    filtered_text = [w for w in words if not w.lower() in stop_words]
    filtered_text = []
    
    for w in words:
        if w not in stop_words:
            filtered_text.append(w)
    
    return Counter(filtered_text)                                         # How often each word occurs


# Will change to import csv
X = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible."
Y = "Bees are flying insects closely related to wasps and ants, known for their role in pollination and, in the case of the best-known bee species, the western honey bee, for producinghoney. Bees are a monophyletic lineage within the superfamily Apoidea. They are presently considered a clade, called Anthophila. There are over 16,000 known species of bees in seven recognized biological families. Some species – including honey bees, bumblebees, and stingless bees – live socially in colonies while some species – including mason bees, carpenter bees, leafcutter bees, and sweat bees – are solitary."

#vector1 = text_to_vector(X)
#vector2 = text_to_vector(Y)

#cosine = get_cosine(vector1, vector2)
#print("Cosine similarity score is:", round(cosine,3))