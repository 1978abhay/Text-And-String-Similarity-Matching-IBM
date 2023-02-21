from flask import Flask , render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route('/compare')
def compare():
    return render_template('score.html')



#@app.route("/compare", methods=["POST", "GET"])
#def compare():
   # if request.method == "POST":
    #    simscore = request.form["xy"]
    #    return redirect(url_for("score", simscore=score))
    #else:
    #    return render_template("compare.html")
#@app.route("/score")
#def score():
#def score (simscore):
   # return f"<h1>{simscore}</h1>"
   # return "hello"

if __name__ == "__main__":
    app.run(debug = True)
