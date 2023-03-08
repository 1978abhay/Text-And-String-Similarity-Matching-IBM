import mongeElkan as me
import LevenshteinSimscore as lt
import datasetReader as dr
import checkingifsynonym as checkSyn

if __name__ == "__main__":
    #textB = dr.getStory("clean_bbc_news_list_uk.json", 32)
    #textA = dr.getStory("clean_bbc_news_list_uk.json", 70)
    textA = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible."
    textB = "Bees are flying insects closely related to wasps and ants, known for their role in pollination and, in the case of the best-known bee species, the western honey bee, for producinghoney. Bees are a monophyletic lineage within the superfamily Apoidea. They are presently considered a clade, called Anthophila. There are over 16,000 known species of bees in seven recognized biological families. Some species – including honey bees, bumblebees, and stingless bees – live socially in colonies while some species – including mason bees, carpenter bees, leafcutter bees, and sweat bees – are solitary."
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
    #print(me.longMongeElkan(1, textA, textB, lt.sim_score))
    #print(me.quadSimilarityME(textA, textB, lt.sim_score))

    # binary synonym score 

    print(me.longMongeElkan(1, textA, textB, lambda a,b: int(checkSyn.anotherWord(a,b))))
    print(me.quadSimilarityME(textA, textB, lambda a,b: int(checkSyn.anotherWord(a,b))))
