import numpy as geek
import nltk
import pandas as pd
#This is the code I was working on that uses the levenshtein algorithm to provide a similarity score for the strings I
#used as examples before. However, it is done on a one to one basis so needs to be improved with Peter's new algorithm.
def get_average_wordLength(word):
    counter =0
    for i in range(len(word)):
        counter = counter + len(word[i])
    average = counter/len(word)
    return average
def min_distance(firstWord, secondWord):
    firstWord =[i for i in firstWord]
    firstWord = fix_word_format(firstWord)
    secondWord = [i for i in secondWord]
    secondWord = fix_word_format(secondWord)
    answer = geek.zeros((len(secondWord), len(firstWord)))
    for j in range(len(firstWord)):
        answer[0,j]=j
    for j1 in range(len(secondWord)):
        answer[j1,0]=j1
    if(firstWord[1]!=secondWord[1]):
        answer[1,1]=2
        
    for c in range(1,len(firstWord)):
        for r in range(1, len(secondWord)):
            if(firstWord[c]!=secondWord[r]):
                if(answer[r-1,c]<answer[r, c-1]):
                    answer[r,c]= answer[r-1,c]+1
                else:
                    answer[r,c]= answer[r,c-1]+1 
            else:
                answer[r,c]= answer[r-1,c-1]
    a = len(secondWord)-1
    b= len(firstWord)-1
    return answer[a,b]
def fix_word_format(word):
    newWord = ""
    newWord = newWord+"#"
    for s in range(len(word)):
     newWord = newWord+word[s]
    return newWord
string = "The man looked at the clock. There was a lot of problems that were keeping him awake at night"

a = string.split(' ')
angels =get_average_wordLength(a)
string1 = "The woman peeked at the clone. She had a lot of issues that were halting her wake at night"
b = string1.split(' ')
angels1 =get_average_wordLength(b)
cumulative =0
for f in range(len(b)):
   word= a[f]
   word1 = b[f]
   thesol = min_distance(word,word1)
   cumulative = cumulative + thesol
averageLengthOfWordsInText1 = angels
numberOfWordsInText1 = len(a)
totalNumberOfLettersInText1 = averageLengthOfWordsInText1*numberOfWordsInText1
print(totalNumberOfLettersInText1,"Total number of letters in text1 ",)
print(cumulative, "cumulative number of edits")
ratio = cumulative/ totalNumberOfLettersInText1
finalAnswer =0
if(ratio>0 and ratio<1):
 finalAnswer = 1-ratio
else:
 ratio =0
finalAnswer = finalAnswer*100
print(finalAnswer, "% Similarity by spelling")



                    
    