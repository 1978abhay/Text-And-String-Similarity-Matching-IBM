import numpy as geek
def get_average_wordLength(word):
    counter =0
    for i in range(len(word)):
        counter = counter + len(word[i])-1
    average = counter/len(word)
    return average
def min_distance(firstWord, secondWord):

    firstWord =[i for i in firstWord]
    secondWord = [i for i in secondWord]
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
string = "#22 #was #great"

a = string.split(' ')
angels =get_average_wordLength(a)
string1 = "#22 #is #great"
b = string1.split(' ')
angels1 =get_average_wordLength(b)
cumulative =0
for f in range(len(b)):
   word= a[f]
   word1 = b[f]
   thesol = min_distance(word,word1)
   cumulative = cumulative + thesol
averageLengthOfWordsInText1 = angels
averageLenfthOfWordsInText2 = angels1
numberOfWordsInText1 = len(a)
numberOfWordsInText2 = len(b)
totalNumberOfLettersInText1 = averageLengthOfWordsInText1*numberOfWordsInText1
print(totalNumberOfLettersInText1)
print(cumulative, "cumulative")
ratio = cumulative/ totalNumberOfLettersInText1
finalAnswer =0
if(ratio>0 and ratio<1):
 finalAnswer = 1-ratio
else:
 ratio =0
finalAnswer = finalAnswer*100
print(finalAnswer, "% Ratio")
#totalNumberOfLettersInText2 = averageLenfthOfWordsInText2*numberOfWordsInText2

                    
    