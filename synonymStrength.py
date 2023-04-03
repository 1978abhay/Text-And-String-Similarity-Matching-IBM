from nltk.corpus import wordnet

# define the words and their synsets
word1 = "happy"
word2 = "glad"
synset1 = wordnet.synset(word1 + '.a.01')
synset2 = wordnet.synset(word2 + '.a.01')

# calculate the Wu-Palmer Similarity score
score = synset1.wup_similarity(synset2)

# print the score
print(score)