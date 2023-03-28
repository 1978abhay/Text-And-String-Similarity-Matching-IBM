from flask import Flask, render_template, redirect
import cosine
import jaccard
import json
import mongeElkan as me
import LevenshteinSimscore as lt
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
    string1Vect = cosine.text_to_vector(string1)
    string2Vect = cosine.text_to_vector(string2)
    cosineans = cosine.get_cosine(string1Vect, string2Vect)

    print("string1 : ", string1, "string2 : ", string2)
    print("cosine result is ", cosineans)

    jaccardans = jaccard.jaccard_index(string1, string2)

    print("jaccard result is: ", jaccardans)

    longmongeelkan = me.longMongeElkan(1, string1, string2, lt.sim_score)
    print("longmongeelkan result is: ", longmongeelkan)
    tfidf = tf.bert(string1, string2)
    print("tf_idf result is: ", tfidf)

    review = summariser.summarise(string1 + string2, 1)
    print("Summary: " + review)

    nlp = spacy.load('en_core_web_lg')
    str1 = nlp(string1)
    str2 = nlp(string2)
    str1_2 = str1.similarity(str2)
    print("Spacy result is: ", str1_2)

    averagescore = round(statistics.median_high(sorted([jaccardans, cosineans, longmongeelkan, tfidf])), 3)
    print("Average score:", averagescore)

    results = {
        "cosine": cosineans,
        "jaccard": jaccardans,
        "lmongeelkan": longmongeelkan,
        "tfidf": tfidf,
        "spacy": str1_2,
        "summary": review,
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

if __name__ == "__main__":
    app.run(debug=True)
