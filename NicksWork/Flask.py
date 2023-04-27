from flask import Flask, render_template, jsonify, request
import pickle as pkl
from songsInterface import SONGSINTERFACE
app = Flask(__name__)

songs = pkl.load(open("NicksWork/songsDictListPickle.pkl", 'rb'))


@app.route("/")
def home():
    songs = pkl.load(open("NicksWork/songsDictDictPickle.pkl", 'rb'))
    return render_template("home.html", songs=songs)

@app.route('/process-data', methods=['POST'])
def process_data():
    data = request.get_json()
    songs = pkl.load(open("NicksWork/songsPickle.pkl", 'rb'))
    SI = SONGSINTERFACE(songs)
    curPrompt = SI.returnPromptWithList(songList=data)

    # Process the data
    return {'message': curPrompt}


@app.route("/about")
def about():
    return render_template("about.html")
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
