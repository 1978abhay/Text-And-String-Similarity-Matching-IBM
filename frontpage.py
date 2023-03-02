import requests
from flask import Flask, session, render_template, redirect, url_for, request, jsonify
import json
import cosine

app = Flask(__name__)

compresult = ""
@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route('/compare')
def compare():
    return render_template('score.html')


@app.route('/about')
def about():
    return render_template('infopage.html')


@app.route('/rerouter')
def rerouter():
    return redirect('/')


@app.route('/testFunc/<string:string1>/<string:string2>')
def tryprocess(string1, string2):
    string1Vect = cosine.text_to_vector(string1)
    string2Vect = cosine.text_to_vector(string2)
    compresult = cosine.get_cosine(string1Vect, string2Vect)

    print("string1 : ", string1, "string2 : ", string2)
    print("result is ", compresult)


    return str(compresult)

@app.route('/compResult')
def fetchResult():
    print(compresult)
    return str(compresult)

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




