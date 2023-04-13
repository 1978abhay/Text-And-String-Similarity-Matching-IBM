import numpy as geek
def fix_word_format(word):
    newWord = ""
    newWord = newWord+"#"
    for s in range(len(word)):
     newWord = newWord+word[s]
    return newWord
def min_distance(firstWord, secondWord):
    if firstWord == "":
        return len(secondWord)
    elif secondWord == "":
        return len(firstWord)
    
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
    lastRowIndex = len(secondWord)-1
    lastColumnIndex= len(firstWord)-1
    return answer[lastRowIndex,lastColumnIndex]

def sim_score(word, word1):
    if(len(word)> len(word1)):
     lengthOfLongestWord = len(word)
    elif len(word) < len(word1):
     lengthOfLongestWord = len(word1)
    else:
        if len(word) == 0:
            return 1
        else:
            lengthOfLongestWord = len(word)
    numberOfEdits =min_distance(word,word1)
    if(numberOfEdits>lengthOfLongestWord):
      return 0
    else:
        simScore = 1-(numberOfEdits/lengthOfLongestWord)
        return simScore

if __name__ == "__main__":
    print(sim_score("party","parties"))
