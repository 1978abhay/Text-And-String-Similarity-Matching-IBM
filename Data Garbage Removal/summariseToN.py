import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from collections import defaultdict
import heapq
import re

def summarise(text, n):
    sentences = sent_tokenize(text) # Tokenise the text into sentences
    ps = PorterStemmer() #Algorithm to reduce words to their root. The idea is that we want to count words like "go" and "going" as the same thing.
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
    sentence_frequencies = defaultdict(int)
    for sentence in sentences:
        for word in word_tokenize(sentence):
            if ps.stem(word.lower()) in word_frequencies:
                sentence_frequencies[sentence] += word_frequencies[ps.stem(word.lower())]

    # Select the top n sentences based on their earlier score
    summary_sentences = heapq.nlargest(n, sentence_frequencies, key=sentence_frequencies.get)

    # Sort the selected sentences in their original order
    summary_sentences = sorted(summary_sentences, key=lambda sentence: sentences.index(sentence))
    
    # Capitalise the first letter of the summary sentences
    summary = ". ".join([re.sub(r'\s([\.\?\!])', r'\1', sentence.capitalize()) for sentence in summary_sentences])


    return summary

# temporary function to test functionality
def go():
    text = """
    The missile knows where it is at all times. It knows this because it knows where it isn't. By subtracting where it is from where it isn't, or where it isn't from where it is (whichever is greater), it obtains a difference, or deviation. The guidance subsystem uses deviations to generate corrective commands to drive the missile from a position where it is to a position where it isn't, and arriving at a position where it wasn't, it now is. Consequently, the position where it is, is now the position that it wasn't, and it follows that the position that it was, is now the position that it isn't. In the event that the position that it is in is not the position that it wasn't, the system has acquired a variation, the variation being the difference between where the missile is, and where it wasn't. If variation is considered to be a significant factor, it too may be corrected by the GEA. However, the missile must also know where it was. The missile guidance computer scenario works as follows. Because a variation has modified some of the information the missile has obtained, it is not sure just where it is. However, it is sure where it isn't, within reason, and it knows where it was. It now subtracts where it should be from where it wasn't, or vice-versa, and by differentiating this from the algebraic sum of where it shouldn't be, and where it was, it is able to obtain the deviation and its variation, which is called error.
    """

    summary = summarise(text, 3)
    print(summary)

# temporary function to display all the stopwords in use
def show_stopwords():
    stops = set(stopwords.words('english'))
    print(stops)
    
# temporary function to test the Porter Stemmer algorithm
def pstest():
    ps = PorterStemmer()
    print(ps.stem("driving"))
