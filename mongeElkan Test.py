import mongeElkan as me
import LevenshteinSimscore as lt
import datasetReader as dr
import checkingifsynonym as checkSyn

if __name__ == "__main__":
    textB = dr.getStory("clean_bbc_news_list_uk.json", 32)
    textA = dr.getStory("clean_bbc_news_list_uk.json", 70)
    wordDict = {}
    for word in [*textB.split(" "),*textA.split(" ")]:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1

    IGNORE_TOP_COMMON_WORDS = 0

    for word in sorted(wordDict.keys(), key = lambda x: wordDict[x])[-IGNORE_TOP_COMMON_WORDS:]:
        textA = textA.replace(word,"")
        textB = textB.replace(word,"")

    while "  " in textA:
        textA = textA.replace("  ", " ")
    while "  " in textB:
        textB = textB.replace("  ", " ")
##    print(textA,"\n")
##    print(textB)

    # levenshtein score
##    print(me.longMongeElkan(1, textA, textB, lt.sim_score))
##    print(me.quadSimilarityME(textA, textB, lt.sim_score))

    # binary synonym score 

    print(me.longMongeElkan(1, textA, textB, lambda a,b: int(checkSyn.anotherWord(a,b))))
    print(me.quadSimilarityME(textA, textB, lambda a,b: int(checkSyn.anotherWord(a,b))))
