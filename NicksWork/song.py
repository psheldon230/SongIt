class SONG:
    def __init__(self, string):

        self.artist = None
        self.songName = None
        self.songArtistName = None
        self.bpm = None
        self.key = None
        self.predominantVoiceGender = None
        self.voicePresenceProfile = None
        self.genreTags = None
        self.genreMean = None
        self.subgenreTags = None
        self.subgenreMean =None
        self.moodTags = None
        self.moodMean = None
        self.moodAdvancedTags = None
        self.moodAdvancedMean = None
        self.characterTags = None
        self.characterMean = None
        self.movementTags = None
        self.movementMean = None
        self.valenceMean = None
        self.arousalMean = None
        self.energyLevel = None
        self.emotionalProfile = None
        self.energyDynamics = None
        self.instrumentTags = None
        self.instrumentPresence = None
        self.meter = None
        self.musicalEra = None
        self.processString(string)

    def processString(self, string):
        lines = string.split("\n")
        artistTitle = lines[0]
        self.songArtistName = artistTitle
        self.artist = artistTitle.split(" - ")[0]
        self.songName = artistTitle.split(" - ")[-1]
        self.bpm = int(lines[1])
        self.key = lines[2]
        self.predominantVoiceGender = lines[3]
        self.voicePresenceProfile = lines[4]
        self.genreTags, self.genreMean = self.splitMeans(lines[6])
        self.subgenreTags, self.subgenreMean = self.splitMeans(lines[8])
        self.moodTags, self.moodMean = self.splitMeans(lines[10])
        self.moodAdvancedTags, self.moodAdvancedMean = self.splitMeans(lines[12])
        self.characterTags, self.characterMean = self.splitMeans(lines[14])
        self.valenceMean = float(lines[17])
        self.arousalMean = float(lines[18])
        self.energyLevel = lines[19]
        self.emotionalProfile = lines[20]
        self.energyDynamics = lines[21]
        self.movementTags,self.movementMean = self.splitMeans(lines[16])
        self.instrumentTags = self.splitInstromentss(lines[23])
        self.meter = lines[25]
        self.musicalEra = lines[26]
        nick = 5

    def splitCapitals(self, string):
        string = string.split("Show all")[0]
        items = []
        prevCap = 0
        for i, ltr in enumerate(string):
            if ltr.isupper() and i != 0:
                items.append(string[prevCap:i])
                prevCap = i
        items.append(string[prevCap:i + 1])
        return items
    
    def splitInstromentss(self, string):
        string = string.split("Show all")[0]
        items = []
        prevCap = 0
        for i, ltr in enumerate(string):
            if ltr.isupper() and i != 0 and string[i - 1] != " ":
                items.append(string[prevCap:i])
                prevCap = i
        items.append(string[prevCap:i + 1])
        return items
    
    def splitMeans(self, string):
        string = string.split("Show all")[0]
        items = []
        keys = []
        if string == "-":
            return keys, items
        prevCap = 0
        for i, ltr in enumerate(string):
            if ltr.isupper() and i != 0 and string[i -1].isnumeric():
                subString = string[prevCap:i]
                splitSubstring = subString.split(": ")
                curKey = splitSubstring[0]
                keys.append(curKey)
                curValue = float(splitSubstring[1])
                items.append((curKey, curValue))
                prevCap = i
        subString = string[prevCap:i + 1]
        splitSubstring = subString.split(": ")
        curKey = splitSubstring[0]
        curValue = float(splitSubstring[1])
        items.append((curKey, curValue))
        keys.append(curKey)
        return keys, items

        


"""The class SONG contains an __init__ method that initializes various attributes of the song object.
string is a parameter passed to the constructor method, which is a string that contains information about the song.
The processString() method is called in the __init__ method to parse the string and populate the attributes of the song object.
Attributes:
The various attributes of the song object are:

artist: The name of the artist of the song.
songName: The name of the song.
songArtistName: The name of the song and artist together.
bpm: The beats per minute of the song.
key: The key of the song.
predominantVoiceGender: The gender of the predominant voice in the song.
voicePresenceProfile: The presence of the voice in the song.
genreTags: The tags for the genre of the song.
genreMean: The means for the genre tags.
subgenreTags: The tags for the sub-genre of the song.
subgenreMean: The means for the sub-genre tags.
moodTags: The tags for the mood of the song.
moodMean: The means for the mood tags.
moodAdvancedTags: The advanced tags for the mood of the song.
moodAdvancedMean: The means for the advanced mood tags.
characterTags: The tags for the character of the song.
characterMean: The means for the character tags.
movementTags: The tags for the movement in the song.
movementMean: The means for the movement tags.
valenceMean: The mean for the valence of the song.
arousalMean: The mean for the arousal of the song.
energyLevel: The energy level of the song.
emotionalProfile: The emotional profile of the song.
energyDynamics: The energy dynamics of the song.
instrumentTags: The tags for the instruments used in the song.
instrumentPresence: The presence of the instruments in the song.
meter: The meter of the song.
musicalEra: The era of the song.
Methods:
The class contains the following methods:

processString(): This method parses the string passed to the constructor and sets the attributes of the song object.
splitCapitals(): This method is used to split the string based on capital letters.
splitInstromentss(): This method is used to split the string based on instruments.
splitMeans(): This method is used to split the string based on means.
The code parses a sample string representing a song and sets the attributes of the song object accordingly. Finally, it creates an object of the SONG class using the sample string.




"""