from nltk.corpus import wordnet
#This file contains a function which returns true or false whether the two words are synonyms or not
def anotherWord(word, word1):
    answer = False
    synonyms = []
    #antonyms = []
    
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            #if l.antonyms():
            # antonyms.append(l.antonyms()[0].name())
    
  #  print(set(synonyms))
    for i in range(len(synonyms)):
        if(synonyms[i]==word1):
            answer = True
            break
    return answer
print(anotherWord("good","bad"))