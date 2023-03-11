# Creating tests that assert that the similarity matching algorithms return the same value on identical strings
from cosine import *

# Testing the cosine similarity matching algorithm against two identical strings
def test_cosine():
    X = Y = text_to_vector("According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.")
    assert round(get_cosine(X,Y), 3)==1.0
    
    
def test_placeholder():
    pass
