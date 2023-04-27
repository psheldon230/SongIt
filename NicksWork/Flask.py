from flask import Flask, render_template, jsonify
import pickle as pkl
app = Flask(__name__)

songs = pkl.load(open("NicksWork/songsDictPickle.pkl", 'rb'))


@app.route("/")
def home():
    songs = jsonify(songs)
    return render_template("home.html", songs=songs)


@app.route("/about")
def about():
    return render_template("about.html")
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
