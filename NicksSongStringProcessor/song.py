class SONG:
    def __init__(self, string):

        self.artist = None
        self.songName = None
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

        
        
sampleString = """Bring Me The Horizon - Can You Feel My Heart
128
E minor
Male
High
RockMetal
Rock: 0.64Metal: 0.49Electronic Dance: 0.04Show all
Indie/AlternativeMetalcore
Indie/Alternative: 0.63Psychedelic Progressive Rock: 0.35Metalcore: 0.35Show all
EnergeticEpicUplifting
Energetic: 0.91Epic: 0.8Uplifting: 0.58Show all
ConfidentMotivationalResoluteShow all
Confident: 0.59Motivational: 0.55Resolute: 0.54Show all
PowerfulRetroHeroicShow all
Powerful: 0.29Retro: 0.26Heroic: 0.19Show all
DrivingRunning
Driving: 0.72Running: 0.55Stomping: 0.32Show all
-0.05
0.90
High
Balanced
Low
Low
Bass GuitarElectric GuitarPercussionShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
contemporary
-
-
0WSa1sucoNRcEeULlZVQXj
Listen on Spotify
|
Similarity
"""
