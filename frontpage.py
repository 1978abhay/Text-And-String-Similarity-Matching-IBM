from flask import Flask, render_template, redirect
from nltk import word_tokenize
from nltk.corpus import stopwords

import cosine
import jaccard
import json
import mongeElkan as me
import LevenshteinSimscore as lt
import checkingifsynonym as checkSyn
import tf_idf as tf
import spacy
import Data_Garbage_Removal.summariseToN as summariser
import statistics

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route('/compare')
def compare():
    return render_template("score.html")

@app.route('/summary')
def summary():
    return render_template("summary.html")


@app.route('/about')
def about():
    return render_template("infopage.html")


@app.route('/rerouter')
def rerouter():
    return redirect('/')


@app.route('/testFunc/<string:string1>/<string:string2>')
def tryprocess(string1, string2):
    review = summariser.scale_summary(string1, string2)
    print(review)

    stop_words = stopwords.words('english')  # Removing stopwords


    input1words = word_tokenize(review[0])
    input2words = word_tokenize(review[1])

    filtered_string1 = [w for w in input1words if not w.lower() in stop_words]
    filtered_string2 = [w for w in input2words if not w.lower() in stop_words]
    filtered_string1 = []
    filtered_string2 = []

    for w in input1words:
        if w not in stop_words:
            filtered_string1.append(w)
    for w in input2words:
        if w not in stop_words:
            filtered_string2.append(w)

    filtered_string1 = ' '.join(filtered_string1)
    filtered_string2 = ' '.join(filtered_string2)

    print(filtered_string1)
    print(filtered_string2)

    first_sum_reduction = str(round((review[4] / review[2]) * 100, 3)) + '%'
    second_sum_reduction = str(round((review[5] / review[3]) * 100, 3)) + '%'

    string1Vect = cosine.text_to_vector(filtered_string1)
    string2Vect = cosine.text_to_vector(filtered_string2)
    cosineans = cosine.get_cosine(string1Vect, string2Vect)

    print("cosine result is ", cosineans)

    jaccardans = jaccard.jaccard_index(filtered_string1, filtered_string2)

    print("jaccard result is: ", jaccardans)

    longmongeelkan = me.longMongeElkan(1, filtered_string1, filtered_string2, lt.sim_score)
    print("longmongeelkan result is: ", longmongeelkan)

    synonymmongeelkan = me.quadSimilarityME(filtered_string1, filtered_string2, lambda a, b: int(checkSyn.is_synonym(a, b)))

    tfidf = tf.bert(review[0], review[1])
    print("tf_idf result is: ", tfidf)


    topsentences = summariser.summarise(string1 + string2, 5)
    print(topsentences)

    averagescore = round(((jaccardans + cosineans + longmongeelkan + (tfidf*4) + synonymmongeelkan)/8), 3)
    print("Average score:", averagescore)

    results = {
        "cosine": cosineans,
        "jaccard": jaccardans,
        "lmongeelkan": longmongeelkan,
        "tfidf": tfidf,
        "synomongeelkan": synonymmongeelkan,
        "first_summary": review[0],
        "second_summary": review[1],
        "first_reduction": first_sum_reduction,
        "second_reduction": second_sum_reduction,
        "average": averagescore
    }

    return json.dumps(results)


#
# @app.route("/compare", methods=["POST", "GET"])
# def compare():
# if request.method == "POST":
#    simscore = request.form["xy"]
#    return redirect(url_for("score", simscore=score))
# else:
#    return render_template("compare.html")
# @app.route("/score")
# def score():
# def score (simscore):
# return f"<h1>{simscore}</h1>"
# return "hello"

# regex.txt first regex very important :   <.*?>

if __name__ == "__main__":
    app.run(debug=True)
