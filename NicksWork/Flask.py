from flask import Flask, render_template, jsonify, request
import pickle as pkl
from spotifyImages import SPOTIFYINTERFACE
from songsInterface import SONGSINTERFACE
import os

app = Flask(__name__)

songs = pkl.load(open("NicksWork/songsDictListPickle.pkl", 'rb'))


@app.route("/")
def home():
    songs = pkl.load(open("NicksWork/songsDictDictPickle.pkl", 'rb'))
    return render_template("fancy.html", songs=songs)


@app.route('/process-data', methods=['POST'])
def process_data():
    data = request.get_json()
    print(data)
    specializedText = data['text']
    songList = data['selectedValues']
    songs_file = "NicksWork/songsPickle.pkl"
    si_file = "NicksWork/SIPickle.pkl"

    # Check if pickle file for SI exists
    if os.path.isfile(si_file):
        # Load SI from the pickle file
        SI = pkl.load(open(si_file, 'rb'))
    else:
        # Load songs from the pickle file
        songs = pkl.load(open(songs_file, 'rb'))

        # Create new instance of SONGSINTERFACE class
        SI = SONGSINTERFACE(songs)

        # Save SI to new pickle file
        with open(si_file, 'wb') as f:
            pkl.dump(SI, f)
    curPrompt = SI.returnPromptWithList(songList=songList, songAdditionalRequest= specializedText)
    curResponce = SI.returnGBTResponce(2000)
    # return {'message': curPrompt}
    return {'message': curResponce}


@app.route('/process-data-update-song', methods=['POST'])
def process_data_update_song():
    data = request.get_json()
    updatedInstructions = data['updatedInstructions']
    previousSong = data['previousSong']
    print(data)
    si_file = "NicksWork/SIPickle.pkl"
    songs_file = "NicksWork/songsPickle.pkl"
    # Check if pickle file for SI exists
    if os.path.isfile(si_file):
        # Load SI from the pickle file
        SI = pkl.load(open(si_file, 'rb'))
    else:
        # Load songs from the pickle file
        songs = pkl.load(open(songs_file, 'rb'))

        # Create new instance of SONGSINTERFACE class
        SI = SONGSINTERFACE(songs)

        # Save SI to new pickle file
        with open(si_file, 'wb') as f:
            pkl.dump(SI, f)
    newSong = SI.updateChatGBT(updatedInstructions=updatedInstructions,previousSong=previousSong)

        

    
    return {'message': newSong}


@app.route("/about")
def about():
    return render_template("about.html")
    return "Hello, World!"


@app.route("/process-album-cover-data",  methods=['POST'])
def processAlbumCoverData():
    SPI = SPOTIFYINTERFACE()
    songList = request.get_json()
    songList.reverse()
    print(songList)
    albumCovers = []

    baseAlbumCover = SPI.searchAlbumCover300("Changes Shrek 2")
    for i in range(5):
        albumCovers.append(baseAlbumCover)

    for i, searchStr in enumerate(songList):
        albumCovers[i] = SPI.searchAlbumCover300(searchStr)

    songs_file = "NicksWork/songsPickle.pkl"
    si_file = "NicksWork/SIPickle.pkl"

    # Check if pickle file for SI exists
    if os.path.isfile(si_file):
        # Load SI from the pickle file
        SI = pkl.load(open(si_file, 'rb'))
    else:
        # Load songs from the pickle file
        songs = pkl.load(open(songs_file, 'rb'))

        # Create new instance of SONGSINTERFACE class
        SI = SONGSINTERFACE(songs)

        # Save SI to new pickle file
        with open(si_file, 'wb') as f:
            pkl.dump(SI, f)

    SI.selectLastSelectedSongsFromList(songList)
    greetings = SI.lastSelectedSongs
    curSongDict = {}
    for song in greetings:
        curSongDict[song.songArtistName] = vars(song)
    
    
    return {'message': albumCovers, "songsDict": curSongDict}



if __name__ == "__main__":
    app.run(debug=True)
