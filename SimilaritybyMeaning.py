from nltk.corpus import wordnet
#This code just checks if the words in 2 strings of same length are synonms and returns percentage that are which constitutes similarity score.
#Again done on 1 to one basis so needs to be improved with Peter's new algorithm.
def get_average_wordLength(word):
    counter =0
    for i in range(len(word)):
        counter = counter + len(word[i])
    average = counter/len(word)
    return average
string = "The man looked at the clock. There was a lot of problems that were keeping him awake at night"
a = string.split(' ')
angels =get_average_wordLength(a)
string1 = "The woman peeked at the clone. She had a lot of issues that were halting her wake at night"
b = string1.split(' ')
angels1 =get_average_wordLength(b)
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
averageLengthOfWordsInText1 = angels
averageLenfthOfWordsInText2 = angels1
numberOfWordsInText1 = len(a)
numberOfWordsInText2 = len(b)
totalNumberOfLettersInText1 = averageLengthOfWordsInText1*numberOfWordsInText1
thecounter=0
for z in range(numberOfWordsInText1-1):
    if(anotherWord(a[z],b[z] )==True or a[z]==b[z]):
        thecounter=thecounter+1
thecounter = thecounter/numberOfWordsInText1*100
print(thecounter, "% Similarity by meanings")