# Creating tests that assert that the similarity matching algorithms return the same value on identical strings
from cosine import *
from jaccard import *
from mongeElkan import *
import tf_idf as tf
import numpy
from LevenshteinSimscore import *
import checkingifsynonym as checkSyn


# Testing the cosine similarity matching algorithm against two identical strings
def test_cosine_identical():
    X = Y = text_to_vector(
        "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.")
    assert round(get_cosine(X, Y), 3) == 1.0


# Testing the jaccard similarity matching algorithm against two identical strings
def test_jaccard_identical():
    X = Y = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible."
    assert (jaccard_index(X, Y)) == 1.0


# Testing the Monge Elkan similarity matching algorithm in combination with Levenshtein similarity funciton
def test_mongeelkan_identical():
    X = Y = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible."
    #assert (synonym_monge_elkan(X, Y)) == 1.0
    assert (levenshtein_monge_elkan(X, Y)) == 1.0


# Testing the TF_IDF similarity matching algorithm on identical strings
def test_tfidf_identical():
    X = Y = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible."
    assert (tf.bert(X, Y)) == 1.0
def test_placeholder():
    pass
