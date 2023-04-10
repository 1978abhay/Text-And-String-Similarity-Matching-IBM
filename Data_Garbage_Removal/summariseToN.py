import pandas as pd
import re
import os

import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from collections import defaultdict
import heapq
import re

SIZE_REDUCTION = 0.25

# If the two texts are different sizes, summarises both to within SIZE_REDUCTION many sentences of the smaller text
# returns the following array:
# [0] - the first input text, summarised
# [1] - the second input text, summarised
# [2] - the sentence count of the first text pre-summary
# [3] - the sentence count of the second text pre-summary
# [4] - the new sentence count of the first summarised text
# [5] - the new sentence count of the second summarised text
def scale_summary(t1, t2):

    t1 = clean(t1)
    t2 = clean(t2)
    sen1 = sent_tokenize(t1)
    sen2 = sent_tokenize(t2)
    sen1_size = len(sen1)
    sen2_size = len(sen2)
    word1 = word_tokenize(t1)
    word2 = word_tokenize(t2)

    if ( len(sen1) > len(sen2) ): # if text 1 has more words than text 2, we want to narrow them down to be similar sizes
        desired_size = sen2_size * SIZE_REDUCTION
        desired_size = round(desired_size)
        print(desired_size)
        t1 = summarise(t1, desired_size)
        t2 = summarise(t2, desired_size)

    elif ( len(sen2) > len(sen1) ): # if text 2 has more words than text 1, we want to narrow them down to be similar sizes
        desired_size = sen1_size * SIZE_REDUCTION
        desired_size = round(desired_size)
        print(desired_size)
        t1 = summarise(t1, desired_size)
        t2 = summarise(t2, desired_size)

    # ADDED BY JOE IN THE EVENT NEITHER TEXT IS SIGNIFICANTLY LARGER THAN THE OTHER
    else:
        t1 = summarise(t1, round(sen1_size * SIZE_REDUCTION))
        t2 = summarise(t2, round(sen2_size * SIZE_REDUCTION))

    new1_size = len(sent_tokenize(t1))
    new2_size = len(sent_tokenize(t2))

    inputs = [t1, t2, sen1_size, sen2_size, new1_size, new2_size]
    return inputs
    

def summarise(text, n):

    text = clean(text)
    # Tokenise the text into sentences
    sentences = sent_tokenize(text)
    #Algorithm to reduce words to their root. The idea is that we want to count words like "go" and "going" as the same thing.
    ps = PorterStemmer()
    #List of common words to remove.
    stop_words = set(stopwords.words('english')) #List of common words to remove.

    # Remove stop words, stem the remaining words
    # We consider words that are more common to be worth more, because if they appear frequently in the text, then it is likely those words represent a better summarisation of the 
    #       meaning of the text.
    word_frequencies = defaultdict(int)
    for sentence in sentences:
        words = word_tokenize(sentence)
        for word in words:
            if word.lower() not in stop_words:
                word_frequencies[ps.stem(word.lower())] += 1

    # Calculate the total value of non-stop-words in the sentence to determine how useful the sentence is
    sentence_values = defaultdict(int)
    for sentence in sentences:
        for word in word_tokenize(sentence):
            if ps.stem(word.lower()) in word_frequencies:
                sentence_values[sentence] += word_frequencies[ps.stem(word.lower())]

        if (sentence.count(" ") >= 3):     
            sentence_values[sentence] /= len(word_tokenize(sentence))
        else:
            sentence_values[sentence] = 0     

    # Create an array of the n best sentences in their original order
    ordered = sorted(sentence_values.values())[-n:]
    summary_sentences = []
    for i in range(len(sentences)):
        if sentence_values[sentences[i]] in ordered:
            summary_sentences.append(sentences[i])

    # It is possible for us to have more than n sentences, if we have 2 with the same score.
    #   this loop ensures we have only n.
    while len(summary_sentences) > n:
        lo = sentence_values[summary_sentences[0]]
        lo_string = "";
        for i in range(len(summary_sentences)):
            if sentence_values[summary_sentences[i]] < lo:
                lo = sentence_values[summary_sentences[i]]
                lo_string = summary_sentences[i]
                
        summary_sentences.remove(lo_string)
        
        

    # Remove garbage characters
    summary = " ".join([re.sub(r'\s([\.\?\!])', r'\1', sentence) for sentence in summary_sentences])


    return summary

def clean(text):

    with open("Data_Garbage_Removal/regex.txt","r") as f:
        regexes = [line.split("~") for line in f.read().split("\n")]

    for oldRegex, newRegex in regexes:
        text = re.sub(oldRegex, newRegex, text)
            
    return text

# temporary function to test functionality
def go():
    text1 = """
    Milosevic is running for the 28 December polls as the head of the Socialist Party of Serbia from his prison cell at The Hague.\nThree other suspected war criminals are also contesting the elections. \nMilosevic\u2019s candidacy has alarmed European diplomats and Serbian democrats who helped oust him from power three years ago.\nIn a stark warning, European Union foreign policy envoy Javier Solana said that Brussels expected Serbia to \u201cmake a choice between the past and the future\u201d, as the republic tries to clinch EU membership.\nElection posters of Milosevic in Belgrade have been spat on, defaced and torn down.\nBut he retains his popularity among hardcore Socialists. Analysts said he could very well be elected to parliament.\nMilosevic was dispatched to The Hague in 2001 to face more than 60 charges of war crimes, crimes against humanity and genocide for his role in the wars in Bosnia, Croatia and Kosovo in the 1990s.\nThree other indicted candidates are ultra-nationalist Serbian Radical Party leader Vojislav Seselj, former Yugoslav army chief of staff General Nebojsa Pavkovic and Serbian Deputy Interior Minister Sreten Lukic.\nDemocrats unruffled\nHowever, democratic leaders say that the indicted candidates pose no serious political threat.\n\n\n\n\n\n\u201cSerbia is on its way to Europe. The only question is how fast we will proceed. There is no way to return to isolation\u201d\nMiroljub LabusG17 Plus party leader\n\n\n\n\n\u201cIt will make no impact on the domestic political scene,\u201d Miroljub Labus of the liberal G17 Plus party said.\n\u201cSerbia is on its way to Europe. The only question is how fast we will proceed. There is no way to return to isolation. \u201d\nPolitical analysts predict that a pro-Europe, democratic coalition of the DSS and G17 will get a majority in the 250-seat assembly and reforms designed to bring Serbia closer to Europe will continue.\nKey issue\nBut a key issue for Serbia\u2019s ambitions of joining the European Union is expected to become even more problematic after the polls, namely cooperation with the UN war crimes tribunal at The Hague.\nCentrist parties are against the tribunal, which they blame for fuelling nationalist sentiment with fresh indictments against Serbian generals in advance of the elections.\nLeading moderate candidate, former president Vojislav Kostunica of the Democratic Party of Serbia (DSS), said The Hague was \u201cpoking fun at justice\u201d and repeated his call for a new Serbian law governing Belgrade\u2019s cooperation with the court.\nHis potential coalition partner, Labus, said he was \u201cstrongly in favour\u201d of future war crimes cases being dealt with in Serbian courts.\n"""

    text2 = """
    Mark: Hello everybody, my name is Markiplier and welcome to Five Nights at Freddy's, an indie horror game that you guys suggested, in mass, and I saw that Yamimash played it and he said it was really really good... So I'm very eager to see what is up. And that is a terrifying animatronic bear! Family pizzeria looking for security guard to work the nightshift. Oh...12 a.m. The first night. If I didn't wanna stay the first night, why would I stay any more than... 5... Why I stay any more than two- hello? Okay...
    """

    summary = scale_summary(text1, text2)
    print("text 1:\n" + summary[0] + "\noriginal sentences: ")
    print(summary[2])
    print("current sentences: ")
    print(summary[4])
    print("\n\ntext 2:\n" + summary[1] + "\noriginal sentences: ")
    print(summary[3])
    print("current sentences: ")
    print(summary[5])

# temporary function to display all the stopwords in use
def show_stopwords():
    stops = set(stopwords.words('english'))
    print(stops)
    
# temporary function to test the Porter Stemmer algorithm
def pstest():
    ps = PorterStemmer()
    print(ps.stem("driving"))
