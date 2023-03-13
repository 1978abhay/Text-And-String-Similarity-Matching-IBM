import mongeElkan as me
import LevenshteinSimscore as lt
import checkingifsynonym as checkSyn


# increasing m will make similarities more important than differences
def calcSimilarity(text_a: str, text_b: str, num_ignored_freq_words=0, semantic=False, m=1):
    if num_ignored_freq_words > 0:
        word_dict = {}
        for word in [*text_b.split(" "), *text_a.split(" ")]:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1

        for word in sorted(word_dict.keys(), key=lambda x: word_dict[x])[-num_ignored_freq_words:]:
            text_a = text_a.replace(word, "")
            text_b = text_b.replace(word, "")

        while "  " in text_a:
            text_a = text_a.replace("  ", " ")
        while "  " in text_b:
            text_b = text_b.replace("  ", " ")

    if semantic:
        # binary synonym score (i.e. word is either synonym or not)
        func = lambda a, b: int(checkSyn.is_synonym(a, b))
    else:
        # levenshtein score
        func = lt.sim_score

    return me.longMongeElkan(m, text_a, text_b, func)


if __name__ == "__main__":
    import datasetReader as dr

    textB = dr.getStory("clean_bbc_news_list_uk.json", 32)
    textA = dr.getStory("clean_bbc_news_list_uk.json", 70)
    print(calcSimilarity(textA, textB, 15, True, 2))
