import SimilarityCalculator_ME_LT as mongueElkan
from functools import partial

def getTopNSimSentences(textA, textB, simFunc, n):
    # TO DO: Improve sentence detection. Once regexes applied, can assume form ". "
    sentencesB = textB.split(".")
    sentencesA = textA.split(".")
    similarSentences = []
    for a in sentencesA:
        for b in sentencesB:
            if len(similarSentences) < n:
                similarSentences.append([a,b,simFunc(a,b)])
            else:
                # replaces pair of sentences with lowest similarity score with new pair of sentences
                # if that new pair has a higher score, so by the end the list has the pairs of sentences
                # with the highest similarities.
                smallestSim = [-1,10*10**80]
                for i in range(n):
                    if similarSentences[i][2] < smallestSim[1]:
                        smallestSim = [i,similarSentences[i][2]]
                similarity = simFunc(a,b)
                if smallestSim[1] < similarity:
                    similarSentences[smallestSim[0]] = [a,b,similarity]

    A,B = [i[0] for i in similarSentences], [i[1] for i in similarSentences]
    return [A,B]

def getTopN_ME_Sentences(textA, textB, n, numIgnoredFreqWords=0, semantic=False,m=1):
    return getTopNSimSentences(textA, textB,
                               partial(mongueElkan.calcSimilarity,numIgnoredFreqWords=numIgnoredFreqWords,semantic=semantic,m=m),
                               n)
    
if __name__ == "__main__":
    import datasetReader as dr
    textB = dr.getStory("clean_bbc_news_list_uk.json", 32)
    textA = dr.getStory("clean_bbc_news_list_uk.json", 70)

    print(getTopN_ME_Sentences(textA, textB,5, 15, True, 1))
    
