import random
import os
import openai
random.seed(1)


class SONGSINTERFACE:
    def __init__(self, initualSongs=None, numSongs=10):
        self.allSongs = None
        self.selectedSongs = None
        self.numSongs = numSongs
        self.lastSelectedSongs = None
        self.allSongsDict = None
        self.lastPrompt = None
        if not initualSongs is None:
            self.setupSongs(initualSongs, self.numSongs)
        return

    def returnGBTResponce(self, maxTokens=50):
        openai.api_key = "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"
        # completion = openai.Completion.create(
        #     engine="text-davinci-002",
        #     prompt=self.lastPrompt,
        #     max_tokens=maxTokens,)
        # print(maxTokens)
        # return completion.choices[0].text

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": self.lastPrompt}
            ]
        )
        return completion.choices[0].message.content

    def setupSongs(self, allSongs, numSongs=10):
        self.addAllSongs(allSongs)
        self.choseSongs(numSongs)

    def addAllSongs(self, allSongs):
        self.allSongs = allSongs
        curDict = {}
        for curSong in allSongs:
            curDict[curSong.songArtistName] = curSong
        self.allSongsDict = curDict

    def selectLastSelectedSongsFromList(self, songsList):
        curSongs = []
        for curSong in songsList:
            print(curSong)
            print(self.allSongsDict[curSong])
            curSongs.append(self.allSongsDict[curSong])
        self.lastSelectedSongs = curSongs

    def returnPromptWithList(self, songList):
        print("songlist", songList)
        self.selectLastSelectedSongsFromList(songList)
        return self.returnPrompt()

    def returnPrompt(self):
        result = ""
        result += "\n\n\n"
        result += "\nPlease write a song that takes influence from the following songs with these details about the songs. Give me the lyrics, cords, bpm, key and instroments that the song should be preformed with"
        for song in self.lastSelectedSongs:
            result += "\n"+song.songName + " by" + song.artist + " with bpm " + str(song.bpm) + " with key " + song.key + " with predominant voice gender " + song.predominantVoiceGender + \
                " with genre " + song.genreTags[0] + " with energy level " + song.energyLevel + \
                " with meter " + song.meter + \
                " with mood " + song.moodAdvancedTags[0]
        self.lastPrompt = result
        return result

    def choseSongs(self, numSongs=50):
        self.selectedSongs = random.sample(list(set(self.allSongs)), numSongs)

    def printSongUI(self):
        for i, curSong in enumerate(self.selectedSongs):
            print(str(i) + " : " + curSong.songName + " - " + curSong.artist)

    def userChooseSongs(self, totalSongstoChoose=3):
        songsChosenInt = 0
        selectedSongs = []

        while songsChosenInt < totalSongstoChoose:
            curSongNum = input("Choose Song " + str(songsChosenInt + 1) +
                               " By typing in a number from 0 to " + str(self.numSongs - 1) + "\n")

            if not curSongNum.isnumeric() or int(curSongNum) < 0 or int(curSongNum) >= self.numSongs:
                print("That was an invalid input")
                continue

            curSelectedSong = self.selectedSongs[int(curSongNum)]
            print("You just selected the song" +
                  curSelectedSong.songName + " - " + curSelectedSong.artist)
            songsChosenInt += 1
            selectedSongs.append(curSelectedSong)

        self.lastSelectedSongs = selectedSongs

    def printPrompt(self, selectedSongs=None):

        print("\n\n\n")
        print("Please write a song that takes influence from the following songs with these details about the songs. Give me the lyrics, cords, bpm, key and instroments that the song should be preformed with")
        for song in self.lastSelectedSongs:
            print(song.songName + " by" + song.artist + " with bpm " +
                  str(song.bpm) + " with key " + song.key + " with predominant voice gender " + song.predominantVoiceGender + " with genre " + song.genreTags[0] + " with energy level " + song.energyLevel + " with meter " + song.meter + " with mood " + song.moodAdvancedTags[0])
