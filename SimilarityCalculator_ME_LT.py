import mongeElkan as me
import LevenshteinSimscore as lt
import checkingifsynonym as checkSyn

                                                                    # increasing m will make similarities more important than differences
def calcSimilarity(textA, textB, numIgnoredFreqWords=0, semantic=False,m=1):
    if numIgnoredFreqWords != 0:
        wordDict = {}
        for word in [*textB.split(" "),*textA.split(" ")]:
            if word not in wordDict:
                wordDict[word] = 1
            else:
                wordDict[word] += 1

        for word in sorted(wordDict.keys(), key = lambda x: wordDict[x])[-numIgnoredFreqWords:]:
            textA = textA.replace(word,"")
            textB = textB.replace(word,"")

        while "  " in textA:
            textA = textA.replace("  ", " ")
        while "  " in textB:
            textB = textB.replace("  ", " ")


    if semantic:
        # binary synonym score (i.e. word is either synonym or not)
        func = lambda a,b: int(checkSyn.anotherWord(a,b))
    else:
    # levenshtein score
        func = lt.sim_score

    return me.longMongeElkan(m, textA, textB, func)



if __name__ == "__main__":
    import datasetReader as dr
    textB = dr.getStory("clean_bbc_news_list_uk.json", 32)
    textA = dr.getStory("clean_bbc_news_list_uk.json", 70)
    print(calcSimilarity(textA,textB, 15, True,2))
