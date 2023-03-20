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

SIZE_REDUCTION = 0.8

# If the two texts are dramatically different sizes, summarises both to within SIZE_REDUCTION many sentences of the smaller text
def scale_summary(t1, t2):

    t1 = clean(t1)
    t2 = clean(t2)
    sen1 = sent_tokenize(t1)
    sen2 = sent_tokenize(t2)
    word1 = word_tokenize(t1)
    word2 = word_tokenize(t2)

    if ( len(word1) / len(word2) >= 1.3 ): # if text 1 has 1.3 or more times as many words as text 2, we want to narrow them down to be similar sizes
        desired_size = len(sen2) * SIZE_REDUCTION
        desired_size = round(desired_size)
        t1 = summarise(t1, desired_size)
        t2 = summarise(t2, desired_size)

    elif ( len(word2) / len(word1) >= 1.3 ): # if text 2 has 1.3 or more times as many words as text 1, we want to narrow them down to be similar sizes
        desired_size = len(sen1) * SIZE_REDUCTION
        desired_size = round(desired_size)
        t1 = summarise(t1, desired_size)
        t2 = summarise(t2, desired_size)

    inputs = [t1, t2]
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
                
        sentence_values[sentence] /= len(word_tokenize(sentence))
                

    # Select the top n sentences based on their earlier score
    summary_sentences = heapq.nlargest(n, sentence_values, key=sentence_values.get)

    # Sort the selected sentences in their original order
    summary = sorted(summary_sentences, key=lambda sentence: sentences.index(sentence))
    
    # Remove garbage characters
    summary = " ".join([re.sub(r'\s([\.\?\!])', r'\1', sentence.capitalize()) for sentence in summary_sentences])


    return summary

def clean(text):

    with open("regex.txt","r") as f:
        regexes = [line.split("~") for line in f.read().split("\n")]

    for oldRegex, newRegex in regexes:
        text = re.sub(oldRegex, newRegex, text)
            
    return text

# temporary function to test functionality
def go():
    text = """
    The International Monetary Fund (IMF) has raised its forecast for global growth this year, from 4. 2% to 4. 6%. It said the world economy grew strongly in the first part of this year, mainly thanks to robust growth in Asia. However, the UK was almost unique in having its 2010 growth forecast revised slightly down, while its 2011 forecast was cut by the IMF from 2. 5% to 2. 1%. The IMF also warned risks had increased and there had been a setback in progress towards financial stability. Developed economies have maintained a modest, but steady recovery in the year to date, the supranational agency said. Concerns over the sustainability of government finances in the developed world, especially Greece and others in Europe, were the major threat to global recovery the IMF argued. It said governments should focus on improving their finances, but warned them not to make cutbacks too rapidly. In recent weeks, a number of governments have introduced austerity measures to cut deficit levels.\"Further credible and decisive policy action us needed to resume progress on financial stability and keep the economic recovery on track,\" said Jose Vinals, director of the Fund's monetary and capital markets division. The IMF said that European banks in particular were being affected by the concerns about government debt and so were less wiling to lend to each other. Less credit available to the wider economy could undermine the recovery, it argued. Although contagion to other regions of the world was likely to be limited, there was a risk that Europe's troubles could have a more substantial impact on global economic growth, it said. The IMF significantly raised its 2010 growth forecast for Brazil - to 7. 1% from 5. 5% - as well as for East Asian tiger economies such as South Korea and Taiwan. But the UK's was downgraded to 1. 2% for this year from an earlier forecast of 1. 3%. This made it one of very few countries to have its growth forecast for 2010 downgraded in the report - the IMF's first forecast since publication of George Osborne's emergency budget.\"The IMF doesn't spell out why it is now more gloomy about the UK,\" said the BBC's economics editor Stephanie Flanders.\"But I am assured that last month's Budget is the reason.\"The agency also slightly reduced its 2010 forecast for France, as well as its 2011 forecasts for the Eurozone, Japan, China and Canada. Meanwhile, in a separate report, the IMF called on the US to do more to tackle its budget deficit.\"We see the need for a more ambitious adjustment to stabilise debt than that envisioned by the authorities,\" the Fund said in its mission report, released on Thursday. The report said that the US should target a surplus of 0. 75% of GDP by 2015, compared with a projected deficit of 11% this year - a Herculean task. The agency suggested a number of tax-raising options:cuts in tax credits, particularly for mortgage interest paymentshigher taxes on energya national consumption tax (like VAT)a financial activities taxIt also called on Washington to do more to deal with the projected growing deficit in the social security budget. Among the various negatives for the US economy, the IMF identified:continuing weak consumer spendinglong-term unemploymenta possible double dip in the housing marketthe failure of hundreds of small banks due to losses in commercial real estatetight financing conditions, especially for smaller firmspossible spillover from the European debt crisisThe report was full of praise for the Federal Reserve, saying the US monetary authority ha.\"deftly managed the trade-off between near-term support and medium-term credibility
    """

    summary = summarise(text, 1)
    print(summary)

# temporary function to display all the stopwords in use
def show_stopwords():
    stops = set(stopwords.words('english'))
    print(stops)
    
# temporary function to test the Porter Stemmer algorithm
def pstest():
    ps = PorterStemmer()
    print(ps.stem("driving"))
