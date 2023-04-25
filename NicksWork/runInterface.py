import pickle as pkl
from song import SONG
from songsInterface import SONGSINTERFACE
import random

random.seed(1)

songs = pkl.load(open("NicksWork/songsPickle.pkl", 'rb'))

curSongInterface = SONGSINTERFACE(songs)
curSongInterface.printSongUI()
curSongInterface.userChooseSongs()
curSongInterface.printPrompt()
nick = 5
