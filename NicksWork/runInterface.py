import pickle as pkl
from song import SONG
from songsInterface import SONGSINTERFACE
import random

random.seed(1)

songs = pkl.load(open("NicksWork/songsPickle.pkl", 'rb'))

curSongInterface = SONGSINTERFACE(songs)
curSongInterface.printSongUI()
curSongInterface.userChooseSongs()
gptPrompt = curSongInterface.printPrompt()
#print(gptPrompt)

with open('BlakeAndPete/gptPrompt.pkl', 'wb') as f:
    pkl.dump(gptPrompt, f)


nick = 5
