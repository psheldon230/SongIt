from song import SONG
import pandas as pd
songsStrings = [
    """Bring Me The Horizon - Can You Feel My Heart
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
Similarity""",
    """100 gecs x Dylan Brady x Laura Les - money machine
99
F# major
Female
  High
RnBPopFunk/SoulShow all
RnB: 0.59Pop: 0.58Funk/Soul: 0.49Show all
-
-
EnergeticSexyHappyShow all
Uplifting: 0.86Energetic: 0.8Sexy: 0.54Show all
ConfidentCoolEnergeticShow all
Confident: 0.47Cool: 0.41Energetic: 0.36Show all
CoolSparkling
Cool: 0.52Sparkling: 0.47Powerful: 0.28Show all
Bouncy
Bouncy: 0.89Groovy: 0.33Pulsing: 0.08Show all
0.65
0.76
  High
Positive
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
late 2000s / contemporary
-
-
61bwFjzXGG1x2aZsANdLyl
Listen on Spotify
|
Similarity""",
    """girl in red - bad idea!
162
C# minor
Female
  High
PopRockLatin
Pop: 0.77Rock: 0.58Latin: 0.44Show all
Indie/Alternative
Indie/Alternative: 0.8Punk: 0.18Pop Soft Rock: 0.15Show all
EnergeticHappyUplifting
Energetic: 0.82Happy: 0.79Uplifting: 0.68Show all
UpliftingUpbeatInspirationalShow all
Uplifting: 0.7Upbeat: 0.65Inspirational: 0.63Show all
Sparkling
Sparkling: 0.41Cool: 0.26Warm: 0.18Show all
DrivingRunningSteadyShow all
Driving: 0.69Running: 0.55Steady: 0.39Show all
0.66
0.56
  High
Positive
  Low
  Low
BassBass GuitarElectric GuitarShow all
Acoustic Guitar: ThroughoutBass: ThroughoutBass Guitar: ThroughoutShow all
4/4
contemporary
-
-
57j65yC2HggQfmYNc6rdOK
Listen on Spotify
|
Similarity""",
    """Bring Me The Horizon - Sleepwalking
149
D minor
Male
  High
MetalRock
Metal: 0.77Rock: 0.41Electronic Dance: 0.02Show all
Indie/AlternativeMetalcore
Metalcore: 0.87Indie/Alternative: 0.54Hard Rock: 0.47Show all
AggressiveEnergeticUplifting
Energetic: 0.94Aggressive: 0.67Uplifting: 0.64Show all
PowerfulStrongResoluteShow all
Powerful: 0.63Strong: 0.6Resolute: 0.59Show all
PowerfulEpicUnpolished
Powerful: 0.82Epic: 0.7Unpolished: 0.7Show all
Driving
Driving: 0.57Running: 0.35Stomping: 0.33Show all
-0.06
0.94
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
0gchQwxmBWj5no8NJ8b2yH
Listen on Spotify
|
Similarity""",
    """Bring Me The Horizon - Shadow Moses
143
Bb minor
Male
  High
Metal
Metal: 0.77Rock: 0.36Electronic Dance: 0.02Show all
Metalcore
Metalcore: 0.91Heavy Metal: 0.08Nu Metal: 0.05Show all
AggressiveEnergeticUplifting
Energetic: 0.95Aggressive: 0.7Uplifting: 0.64Show all
ConfidentMotivationalDeterminedShow all
Confident: 0.57Motivational: 0.54Determined: 0.52Show all
PowerfulEpicUnpolishedShow all
Powerful: 0.81Epic: 0.76Unpolished: 0.47Show all
StompingDriving
Stomping: 0.72Driving: 0.49Pulsing: 0.13Show all
-0.07
0.94
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
68osIGtVjM7QWVe6pazLHj
Listen on Spotify
|
Similarity""",
    """Beach Bunny - Good Girls (Don’t Get Used)
150
Eb major
Female
  High
RockPopSinger/Songwriters
Rock: 0.82Pop: 0.63Singer/Songwriters: 0.55Show all
FolkIndie/Alternative
Indie/Alternative: 0.74Punk: 0.55Country: 0.5Show all
EnergeticHappyUplifting
Energetic: 0.8Happy: 0.7Uplifting: 0.69Show all
ConfidentUpbeatUpliftingShow all
Confident: 0.63Upbeat: 0.6Uplifting: 0.57Show all
Playful
Playful: 0.41Powerful: 0.23Unpolished: 0.16Show all
DrivingRunningBouncy
Driving: 0.4Running: 0.33Bouncy: 0.31Show all
0.61
0.77
  High
Positive
  Low
  Low
Bass GuitarElectric GuitarPercussionShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
early / mid 2000s
-
-
0jvtOoxOKJvAjveBSmffHL
Listen on Spotify
|
Similarity""",
    """33kiro x Sukoyomi x p4rkr - i hate it here
103
Db major
Female
  High
PopRap/Hip-Hop
Pop: 0.58Rap/Hip-Hop: 0.49RnB: 0.19Show all
Jazzy Hip-Hop
Jazzy Hip-Hop: 0.27Pop-Rap: 0.24Contemporary RnB: 0.2Show all
Sexy
Sexy: 0.7Uplifting: 0.38Energetic: 0.34Show all
SeductiveSexyCoolShow all
Seductive: 0.67Sexy: 0.65Cool: 0.58Show all
Cool
Cool: 0.67Bold: 0.3Luxurious: 0.26Show all
Groovy
Groovy: 0.52Bouncy: 0.35Flowing: 0.3Show all
0.49
0.05
Medium
Positive
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
contemporary
-
-
6n1ZjksfQve7uEkxGOiYgA
Listen on Spotify
|
Similarity""",
    """Adele - Rumour Has It
120
D minor
Male
  High
RockPop
Rock: 0.63Pop: 0.59Funk/Soul: 0.29Show all
Indie/Alternative
Indie/Alternative: 0.67Psychedelic Progressive Rock: 0.33Pop Soft Rock: 0.25Show all
EnergeticEpic
Epic: 0.85Energetic: 0.77Uplifting: 0.48Show all
SeriousEmotionalPassionateShow all
Emotional: 0.51Serious: 0.51Passionate: 0.5Show all
Mysterious
Mysterious: 0.75Retro: 0.56Cool: 0.42Show all
StompingDrivingPulsing
Stomping: 0.85Driving: 0.69Pulsing: 0.54Show all
0.04
0.74
  High
Balanced
  Low
  Low
PercussionStringsBass Guitar
Bass Guitar: ThroughoutPercussion: ThroughoutStrings: ThroughoutShow all
4/4
late 2000s / contemporary
-
-
5mFMb5OHI3cN0UjITVztCj
Listen on Spotify
|
Similarity""",
    """Beach Bunny - Weeds
200
Eb major
Female
  High
RockPop
Rock: 0.6Pop: 0.52Folk/Country: 0.29Show all
Indie/Alternative
Indie/Alternative: 0.68Pop Soft Rock: 0.28Punk: 0.22Show all
EnergeticEpicUplifting
Energetic: 0.86Epic: 0.72Uplifting: 0.61Show all
ConfidentMotivationalAnthemicShow all
Confident: 0.55Motivational: 0.52Anthemic: 0.51Show all
PowerfulHeroicSparkling
Powerful: 0.38Heroic: 0.34Sparkling: 0.29Show all
Stomping
Stomping: 0.66Driving: 0.14Pulsing: 0.07Show all
0.15
0.85
  High
Balanced
  Low
  Low
Bass GuitarElectric GuitarPercussionShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
late 2000s / contemporary
-
-
6p0Nvka9pKB9PYEC8kyc03
Listen on Spotify
|
Similarity""",
    """BAND-MAID - Choose me
90
D minor
Female
  High
MetalRock
Metal: 0.71Rock: 0.6Pop: 0.03Show all
Hard RockMetalcoreHeavy MetalShow all
Hard Rock: 0.63Metalcore: 0.57Heavy Metal: 0.4Show all
AggressiveEnergeticUplifting
Energetic: 0.95Uplifting: 0.71Aggressive: 0.64Show all
EnergeticMotivationalExcitingShow all
Energetic: 0.6Motivational: 0.53Exciting: 0.52Show all
UnpolishedBold
Unpolished: 0.62Bold: 0.44Powerful: 0.24Show all
RunningDriving
Running: 0.82Driving: 0.64Nonrhythmic: 0.2Show all
0.05
0.94
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
130dsYbbXp9jQnETiJ7axI
Listen on Spotify
|
Similarity
""",
    """100 gecs x Dylan Brady x Laura Les - hand crushed by a mallet
170
C# minor
Female
  High
PopElectronic Dance
Pop: 0.65Electronic Dance: 0.43Rap/Hip-Hop: 0.18Show all
Electro
Electro: 0.7Abstract IDM Leftfield: 0.28Synth Pop: 0.18Show all
ChillSexy
Sexy: 0.64Chill: 0.56Uplifting: 0.47Show all
CoolSexySeductiveShow all
Cool: 0.5Sexy: 0.44Seductive: 0.42Show all
CoolMysterious
Cool: 0.61Mysterious: 0.57Unpolished: 0.27Show all
Robotic
Robotic: 0.83Driving: 0.24Stomping: 0.18Show all
0.47
0.22
Medium
Positive
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
mid / late 2000s
-
-
7CUkeiG7QtB7tPU9f8SANS
Listen on Spotify
|
Similarity""",
    """100 gecs x Fall Out Boy x Craig Owens x Nicole Dollanganger - hand crushed by a mallet (Remix) [feat. Fall Out Boy, Craig Owens, Nicole Dollanganger]
174
C# minor
Male
  High
Rock
Rock: 0.62Pop: 0.24Electronic Dance: 0.14Show all
Punk
Punk: 0.57Indie/Alternative: 0.26Hard Rock: 0.23Show all
AggressiveEnergeticUplifting
Energetic: 0.94Aggressive: 0.73Uplifting: 0.65Show all
PowerfulStrongConfidentShow all
Powerful: 0.62Strong: 0.62Confident: 0.59Show all
BoldUnpolishedPowerful
Bold: 0.78Unpolished: 0.76Powerful: 0.7Show all
RunningDriving
Running: 0.73Driving: 0.5Pulsing: 0.16Show all
-0.06
0.94
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
5Mm2CJzNRiICC5MWRWQnBo
Listen on Spotify
|
Similarity""",
    """Linkin Park - In the End
105
Db major
Male
  High
MetalRock
Metal: 0.74Rock: 0.45Electronic Dance: 0.02Show all
Hard RockNu Metal
Nu Metal: 0.9Hard Rock: 0.52Indie/Alternative: 0.45Show all
AggressiveEnergeticUplifting
Energetic: 0.94Aggressive: 0.76Uplifting: 0.54Show all
ConfidentResolutePowerfulShow all
Confident: 0.6Resolute: 0.57Powerful: 0.57Show all
PlayfulCool
Playful: 0.32Cool: 0.28Warm: 0.22Show all
Stomping
Stomping: 0.69Driving: 0.33Pulsing: 0.1Show all
-0.21
0.93
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
60a0Rd6pjrkxjPbaKzXjfq
Listen on Spotify
|
Similarity""",
    """Lil Uzi Vert - 444+222
77
G# minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
Trap
Trap: 0.91Pop-Rap: 0.08Gangsta: 0.07Show all
EnergeticAggressive
Energetic: 0.61Aggressive: 0.6Uplifting: 0.43Show all
SeriousConfidentDeterminedShow all
Serious: 0.55Confident: 0.52Determined: 0.42Show all
Unpolished
Unpolished: 0.57Bold: 0.4Playful: 0.39Show all
BouncyRoboticDrivingShow all
Bouncy: 0.38Robotic: 0.35Driving: 0.29Show all
-0.07
0.49
  High
Balanced
  Low
  Low
Bass GuitarPercussionSynthShow all
Bass: ThroughoutBass Guitar: ThroughoutPercussion: ThroughoutShow all
4/4
contemporary
-
-
1QgTBfRN5m81a5K01qens6
Listen on Spotify
|
Similarity""",
    """blackbear x P-Lo - shake ya ass (feat. P-Lo)
100
D# minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
Pop-Rap
Pop-Rap: 0.69Trap: 0.22Gangsta: 0.21Show all
SexyUplifting
Sexy: 0.69Uplifting: 0.68Chill: 0.49Show all
ConfidentMotivationalEuphoricShow all
Confident: 0.58Motivational: 0.54Euphoric: 0.52Show all
CoolLuxurious
Cool: 0.65Luxurious: 0.53Sophisticated: 0.36Show all
Bouncy
Bouncy: 0.89Groovy: 0.27Flowing: 0.16Show all
0.73
0.40
  High
Positive
  Low
  Low
PercussionSynth
Percussion: ThroughoutSynth: ThroughoutAcoustic Guitar: AbsentShow all
4/4
late 2000s / contemporary
-
-
0quqp7sNqZnyrePWcTPfpi
Listen on Spotify
|
Similarity""",
    """Gucci Mane - Lemonade
142
G minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
Gangsta
Gangsta: 0.69Pop-Rap: 0.23Trap: 0.09Show all
EnergeticSexyUplifting
Uplifting: 0.81Energetic: 0.7Sexy: 0.63Show all
ConfidentDeterminedResoluteShow all
Confident: 0.57Determined: 0.53Resolute: 0.53Show all
PlayfulWarm
Playful: 0.79Warm: 0.54Cool: 0.11Show all
RoboticStompingDriving
Robotic: 0.48Stomping: 0.42Driving: 0.36Show all
0.68
0.69
  High
Positive
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
early / mid 2000s
-
-
0hmQY8NW6hNQWfkvZsa1e9
Listen on Spotify
|
Similarity
""",
    """Rebzyyx x hoshie star - all I want is you
146
B major
Female
  High
Electronic Dance
Electronic Dance: 0.8Pop: 0.28Rock: 0.05Show all
Electro
Electro: 0.59Trance: 0.31Synth Pop: 0.16Show all
EnergeticHappySexyShow all
Uplifting: 0.9Energetic: 0.85Happy: 0.67Show all
EnergeticEuphoricConfidentShow all
Confident: 0.51Energetic: 0.51Euphoric: 0.51Show all
Cool
Cool: 0.63Unpolished: 0.23Luxurious: 0.15Show all
RoboticRunningDriving
Robotic: 0.34Running: 0.33Driving: 0.3Show all
0.67
0.75
  High
Positive
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
contemporary
-
-
7lOvJBqH38ZY59eLU7bioq
Listen on Spotify
|
Similarity""",
    """DJ Scheme x $NOT x Fenix Flexin - Blue Bills (feat. $NOT & Fenix Flexin)
96
G minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
Trap
Trap: 0.66Gangsta: 0.33Pop-Rap: 0.09Show all
EnergeticAggressive
Energetic: 0.72Aggressive: 0.61Uplifting: 0.45Show all
ConfidentDeterminedSeriousShow all
Confident: 0.55Determined: 0.54Serious: 0.53Show all
UnpolishedBoldCool
Unpolished: 0.67Bold: 0.61Cool: 0.5Show all
BouncyGroovy
Bouncy: 0.45Groovy: 0.43Driving: 0.29Show all
-0.10
0.59
  High
Balanced
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
late 2000s / contemporary
-
-
2ODUTBkiOWoYSUjKpGJxQE
Listen on Spotify
|
Similarity""",
    """$uicideboy$ - Memoirs of a Gorilla
110
C major
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.55Electronic Dance: 0.16Reggae: 0.13Show all
Pop-RapTrap
Pop-Rap: 0.65Trap: 0.47Gangsta: 0.16Show all
EnergeticSexyUplifting
Uplifting: 0.77Energetic: 0.68Sexy: 0.62Show all
ConfidentCoolEuphoricShow all
Confident: 0.52Cool: 0.48Euphoric: 0.46Show all
UnpolishedBoldCool
Unpolished: 0.75Bold: 0.73Cool: 0.58Show all
RoboticDriving
Robotic: 0.24Driving: 0.23Running: 0.14Show all
0.58
0.66
  High
Positive
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
contemporary
-
-
32B4HyegZNlYIWhENs8FcZ
Listen on Spotify
|
Similarity""",
    """My Chemical Romance - Famous Last Words
129
D minor
Male
  High
MetalRock
Metal: 0.74Rock: 0.54Electronic Dance: 0.02Show all
Heavy MetalNu MetalDoom MetalShow all
Punk: 0.47Heavy Metal: 0.38Nu Metal: 0.36Show all
EnergeticUplifting
Energetic: 0.9Uplifting: 0.77Happy: 0.41Show all
PowerfulConfidentStrongShow all
Powerful: 0.63Confident: 0.61Strong: 0.61Show all
PowerfulUnpolished
Powerful: 0.8Unpolished: 0.72Epic: 0.49Show all
DrivingRunning
Driving: 0.61Running: 0.52Stomping: 0.28Show all
0.47
0.88
  High
Positive
  Low
  Low
Bass GuitarElectric GuitarPercussionShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
mid / late 2000s
-
-
2d6m2F4I7wCuAKtSsdhh83
Listen on Spotify
|
Similarity""",
    """Disco Lines - Baby Girl
121
F# minor
Female
Medium
Electronic Dance
Electronic Dance: 0.81Pop: 0.18Funk/Soul: 0.07Show all
Deep HouseHouse
House: 0.86Deep House: 0.7Tech House: 0.34Show all
EnergeticSexyHappyShow all
Uplifting: 0.88Energetic: 0.77Sexy: 0.66Show all
ConfidentEnergeticMotivationalShow all
Confident: 0.57Energetic: 0.55Motivational: 0.54Show all
Cool
Cool: 0.7Luxurious: 0.39Sophisticated: 0.11Show all
BouncyDriving
Bouncy: 0.79Driving: 0.67Pulsing: 0.39Show all
0.72
0.69
  High
Positive
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
contemporary
-
-
2cSdAkzAf2T4j4aLvx4LLz
Listen on Spotify
|
Similarity""",
    """21 Savage x Metro Boomin - Glock In My Lap
130
Bb minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.82RnB: 0.06Pop: 0.04Show all
Trap
Trap: 0.8Gangsta: 0.22Pop-Rap: 0.05Show all
DarkScaryEtherealShow all
Dark: 0.88Scary: 0.63Ethereal: 0.6Show all
ConfidentEnergeticMotivationalShow all
Confident: 0.59Energetic: 0.53Motivational: 0.52Show all
BoldUnpolishedCool
Bold: 0.71Unpolished: 0.65Cool: 0.61Show all
DrivingBouncy
Driving: 0.59Bouncy: 0.55Stomping: 0.33Show all
-0.77
0.26
Medium
Negative
  Low
  Low
PercussionSynth
Percussion: ThroughoutSynth: ThroughoutAcoustic Guitar: AbsentShow all
4/4
contemporary
-
-
6pcywuOeGGWeOQzdUyti6k
Listen on Spotify
|
Similarity""",
    """Blur - Song 2
130
F minor
Male
  High
RockMetal
Rock: 0.69Metal: 0.54Singer/Songwriters: 0.05Show all
Indie/AlternativeNu MetalHeavy MetalShow all
Punk: 0.71Indie/Alternative: 0.46Nu Metal: 0.44Show all
AggressiveEnergeticUpliftingShow all
Energetic: 0.93Aggressive: 0.62Uplifting: 0.55Show all
ConfidentPowerfulStrongShow all
Confident: 0.52Powerful: 0.46Strong: 0.44Show all
BoldUnpolishedPowerful
Bold: 0.84Unpolished: 0.75Powerful: 0.65Show all
StompingDriving
Stomping: 0.7Driving: 0.43Running: 0.16Show all
-0.12
0.93
  High
Balanced
  Low
  Low
Bass GuitarElectric GuitarPercussionShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
early / mid 1990s
-
-
3GfOAdcoc3X5GPiiXmpBjK
Listen on Spotify
|
Similarity
""",
    """Rage Against The Machine - Bulls On Parade
84
F minor
Female
  High
Rock
Rock: 0.78Metal: 0.27Blues: 0.18Show all
Hard RockIndie/AlternativePunk
Indie/Alternative: 0.48Hard Rock: 0.42Punk: 0.31Show all
AggressiveEnergetic
Energetic: 0.9Aggressive: 0.79Uplifting: 0.39Show all
PowerfulStrongResoluteShow all
Powerful: 0.61Strong: 0.59Resolute: 0.56Show all
BoldUnpolishedPowerful
Bold: 0.76Unpolished: 0.75Powerful: 0.69Show all
Stomping
Stomping: 0.77Groovy: 0.39Driving: 0.17Show all
-0.39
0.89
  High
Negative
  Low
  Low
PercussionBassBass Guitar
Bass: ThroughoutBass Guitar: ThroughoutPercussion: ThroughoutShow all
4/4
mid / late 1990s
-
-
0tZ3mElWcr74OOhKEiNz1x
Listen on Spotify
|
Similarity""",
    """Ariana Grande - needy
174
Eb major
Female
  High
RnBFunk/SoulRap/Hip-HopShow all
RnB: 0.69Funk/Soul: 0.48Rap/Hip-Hop: 0.47Show all
Neo Soul
Neo Soul: 0.88Soul: 0.17Gospel: 0.02Show all
CalmChillRomanticShow all
Chill: 0.97Calm: 0.9Romantic: 0.79Show all
ThoughtfulEmotionalBittersweetShow all
Emotional: 0.53Thoughtful: 0.53Bittersweet: 0.52Show all
Cool
Cool: 0.69Retro: 0.32Powerful: 0.28Show all
Groovy
Groovy: 0.81Flowing: 0.3Steady: 0.3Show all
0.06
-0.89
  Low
Balanced
  Low
  Low
PercussionBass
Bass: ThroughoutPercussion: ThroughoutAcoustic Guitar: AbsentShow all
4/4
late 2000s / contemporary
-
-
1TEL6MlSSVLSdhOSddidlJ
Listen on Spotify
|
Similarity""",
    """Phoenix - 1901
144
C major
Female
  High
PopElectronic DanceRock
Pop: 0.64Electronic Dance: 0.59Rock: 0.44Show all
ElectroSynth Pop
Synth Pop: 0.53Electro: 0.51House: 0.1Show all
EnergeticUpliftingHappy
Energetic: 0.8Uplifting: 0.65Happy: 0.5Show all
ConfidentMotivationalAnthemicShow all
Confident: 0.62Motivational: 0.57Anthemic: 0.53Show all
Sparkling
Sparkling: 0.34Epic: 0.18Heroic: 0.14Show all
DrivingBouncy
Driving: 0.46Bouncy: 0.44Running: 0.26Show all
0.54
0.79
  High
Positive
  Low
  Low
Bass GuitarElectric GuitarPercussionShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
contemporary
-
-
1mvyqSb1tOvtVP1qfWEyPa
Listen on Spotify
|
Similarity""",
    """Tinashe x ScHoolboy Q - 2 On (feat. ScHoolboy Q)
101
D major
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
Pop-RapTrap
Pop-Rap: 0.58Trap: 0.54Gangsta: 0.24Show all
ChillSexy
Chill: 0.79Sexy: 0.56Ethereal: 0.48Show all
ConfidentDeterminedStrongShow all
Confident: 0.53Determined: 0.51Strong: 0.5Show all
Cool
Cool: 0.79Luxurious: 0.45Warm: 0.44Show all
Bouncy
Bouncy: 0.86Groovy: 0.11Driving: 0.09Show all
0.16
-0.20
Medium
Balanced
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
late 2000s / contemporary
-
-
3jVtllWS5CFFWLQng8sKsr
Listen on Spotify
|
Similarity
""",
    """Fetty Wap x Remy Boyz - 679 (feat. Remy Boyz)
95
E minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
Pop-Rap
Pop-Rap: 0.77Gangsta: 0.38Trap: 0.11Show all
ChillSexyUplifting
Sexy: 0.72Uplifting: 0.65Chill: 0.5Show all
ConfidentUpbeatEuphoricShow all
Confident: 0.56Upbeat: 0.53Euphoric: 0.52Show all
CoolUnpolishedBold
Cool: 0.64Unpolished: 0.64Bold: 0.57Show all
Bouncy
Bouncy: 0.88Groovy: 0.32Driving: 0.13Show all
0.63
0.38
  High
Positive
  Low
  Low
PercussionSynthBassShow all
Bass: ThroughoutBass Guitar: ThroughoutPercussion: ThroughoutShow all
4/4
late 2000s / contemporary
-
-
5NQbUaeTEOGdD6hHcre0dZ
Listen on Spotify
|
Similarity""",
    """The Neighbourhood - Afraid
84
F# minor
Female
  High
RockPopSinger/Songwriters
Rock: 0.67Pop: 0.55Singer/Songwriters: 0.36Show all
Indie/Alternative
Indie/Alternative: 0.78Pop Soft Rock: 0.26Psychedelic Progressive Rock: 0.22Show all
EnergeticEpic
Epic: 0.84Energetic: 0.76Uplifting: 0.42Show all
SeriousConcernedSpiritualShow all
Serious: 0.5Concerned: 0.47Spiritual: 0.45Show all
Epic
Epic: 0.51Powerful: 0.3Unpolished: 0.26Show all
Flowing
Flowing: 0.63Stomping: 0.19Pulsing: 0.12Show all
-0.18
0.72
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
7brQHA2CgQpcMBiOlfiXYb
Listen on Spotify
|
Similarity
""",
    """Bruce Springsteen - Atlantic City
111
F# minor
Male
  High
Rock
Rock: 0.77Blues: 0.33Singer/Songwriters: 0.22Show all
Folk RockPsychedelic Progressive Rock
Psychedelic Progressive Rock: 0.37Folk Rock: 0.34Blues Rock: 0.22Show all
EnergeticEpic
Epic: 0.61Energetic: 0.56Happy: 0.48Show all
SolemnEmotionalThoughtfulShow all
Emotional: 0.51Solemn: 0.51Thoughtful: 0.45Show all
CoolWarmUnpolished
Cool: 0.39Warm: 0.33Unpolished: 0.24Show all
StompingDriving
Stomping: 0.48Driving: 0.47Running: 0.23Show all
0.31
0.48
  High
Positive
  Low
  Low
Acoustic GuitarBass
Acoustic Guitar: ThroughoutBass: ThroughoutBass Guitar: AbsentShow all
4/4
early / mid 1970s
-
-
1Vp8U39YNsDfd6yVuaUq12
Listen on Spotify
|
Similarity""",
    """Bruce Springsteen - Born in the U.S.A.
125
B major
Male
  High
Rock
Rock: 0.85Singer/Songwriters: 0.35Pop: 0.19Show all
Indie/AlternativeHard RockPop Soft Rock
Pop Soft Rock: 0.41Indie/Alternative: 0.37Hard Rock: 0.3Show all
EnergeticUpliftingEpic
Energetic: 0.91Uplifting: 0.74Epic: 0.59Show all
ConfidentMotivationalAnthemicShow all
Confident: 0.57Motivational: 0.54Anthemic: 0.52Show all
SparklingPowerfulHeroic
Sparkling: 0.49Powerful: 0.37Heroic: 0.36Show all
Stomping
Stomping: 0.78Driving: 0.13Steady: 0.12Show all
0.30
0.89
  High
Positive
  Low
  Low
Bass GuitarElectric GuitarPercussionShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
early / mid 1990s
-
-
0dOg1ySSI7NkpAe89Zo0b9
Listen on Spotify
|
Similarity
""",
    """The Whitest Boy Alive - Burning
75
B minor
Male
  High
RockPop
Rock: 0.62Pop: 0.56Latin: 0.37Show all
Indie/Alternative
Indie/Alternative: 0.63Folk Rock: 0.35Pop Soft Rock: 0.22Show all
CalmChillRomanticShow all
Chill: 0.93Romantic: 0.74Calm: 0.7Show all
ThoughtfulSadBittersweetShow all
Thoughtful: 0.54Sad: 0.53Bittersweet: 0.52Show all
SparklingWarm
Sparkling: 0.71Warm: 0.52Ethereal: 0.14Show all
Bouncy
Bouncy: 0.53Steady: 0.34Groovy: 0.28Show all
0.31
-0.67
  Low
Positive
  Low
  Low
BassBass GuitarElectric GuitarShow all
Acoustic Guitar: ThroughoutBass: ThroughoutBass Guitar: ThroughoutShow all
4/4
late 2000s / contemporary
-
-
0QgR03vMDoBoLgcu08EtKl
Listen on Spotify
|
Similarity""",
    """The White Stripes - The Denial Twist
93
C minor
Male
  High
Rock
Rock: 0.55Rap/Hip-Hop: 0.37Blues: 0.24Show all
Blues RockFolk RockIndie/Alternative
Indie/Alternative: 0.48Blues Rock: 0.42Folk Rock: 0.4Show all
Chill
Chill: 0.57Happy: 0.47Ethereal: 0.47Show all
PassionateInspirationalEmotionalShow all
Passionate: 0.5Inspirational: 0.49Emotional: 0.47Show all
Powerful
Powerful: 0.81Unpolished: 0.58Heroic: 0.49Show all
GroovyStomping
Groovy: 0.47Stomping: 0.4Driving: 0.24Show all
0.43
0.20
Medium
Positive
  Low
  Low
PercussionPianoBassShow all
Bass: ThroughoutBass Guitar: ThroughoutPercussion: ThroughoutShow all
4/4
mid / late 2000s
-
-
4Hzg7Hcqo2aUooTQ0pnBYC
Listen on Spotify
|
Similarity
""",
    """The National - Don't Swallow the Cap
87
D minor
Male
  High
PopRockLatin
Pop: 0.69Rock: 0.51Latin: 0.4Show all
Indie/Alternative
Indie/Alternative: 0.84Folk Rock: 0.36Pop Soft Rock: 0.24Show all
EtherealChillCalmShow all
Sad: 0.63Ethereal: 0.61Chill: 0.59Show all
EmotionalSadThoughtfulShow all
Emotional: 0.53Sad: 0.52Thoughtful: 0.52Show all
MysteriousCoolUnpolishedShow all
Mysterious: 0.63Cool: 0.58Unpolished: 0.41Show all
FlowingGroovy
Flowing: 0.3Groovy: 0.26Bouncy: 0.16Show all
-0.59
-0.40
  Low
Negative
  Low
  Low
Bass GuitarElectric GuitarStringsShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
contemporary
-
-
3l3SbRkrK1aQ5Dk1h7vroV
Listen on Spotify
|
Similarity""",
    """Beach Bunny - Entropy
182
Ab major
Female
  High
RockPopSinger/Songwriters
Rock: 0.77Pop: 0.57Singer/Songwriters: 0.4Show all
Indie/Alternative
Indie/Alternative: 0.69Punk: 0.42Pop Soft Rock: 0.25Show all
EnergeticHappyUplifting
Energetic: 0.75Happy: 0.68Uplifting: 0.68Show all
UpliftingConfidentInspirationalShow all
Uplifting: 0.7Confident: 0.63Inspirational: 0.57Show all
PlayfulWarmPowerfulShow all
Playful: 0.31Warm: 0.27Powerful: 0.26Show all
DrivingRunning
Driving: 0.47Running: 0.38Bouncy: 0.21Show all
0.56
0.64
  High
Positive
  Low
  Low
Bass GuitarElectric GuitarPercussionShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
mid / late 2000s
-
-
5Dp8m5EWFkNc3TbCSxKSzu
Listen on Spotify
|
Similarity
""",
    """Foo Fighters - Everlong
158
D major
Male
  High
Rock
Rock: 0.8Pop: 0.26Latin: 0.15Show all
Indie/AlternativeHard RockPunk
Punk: 0.61Indie/Alternative: 0.49Hard Rock: 0.28Show all
AggressiveEnergeticUpliftingShow all
Energetic: 0.95Uplifting: 0.7Aggressive: 0.6Show all
ConfidentMotivationalEnergeticShow all
Confident: 0.6Motivational: 0.57Energetic: 0.55Show all
PowerfulUnpolishedHeroicShow all
Powerful: 0.73Unpolished: 0.59Heroic: 0.46Show all
Driving
Driving: 0.67Running: 0.43Stomping: 0.25Show all
0.03
0.94
  High
Balanced
  Low
  Low
Bass GuitarElectric GuitarPercussionShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
late 2000s / contemporary
-
-
5UWwZ5lm5PKu6eKsHAGxOk
Listen on Spotify
|
Similarity
""",
    """Tracy Chapman - Fast Car
104
A major
Male
  High
Folk/CountryRock
Folk/Country: 0.46Rock: 0.44Pop: 0.27Show all
CountryFolk Rock
Country: 0.76Folk Rock: 0.59Blues Rock: 0.37Show all
RomanticChill
Romantic: 0.62Chill: 0.48Sad: 0.43Show all
WarmContentedSweetShow all
Warm: 0.58Contented: 0.52Sweet: 0.52Show all
Warm
Warm: 0.75Playful: 0.13Sparkling: 0.11Show all
BouncyFlowing
Bouncy: 0.56Flowing: 0.46Groovy: 0.1Show all
-0.13
-0.08
Medium
Balanced
  Low
  Low
Bass GuitarElectric GuitarPercussionShow all
Acoustic Guitar: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
mid / late 1980s
-
-
2M9ro2krNb7nr7HSprkEgo
Listen on Spotify
|
Similarity
""",
    """Calvin Harris - Feel So Close - Radio Edit
128
G major
None
None
Electronic Dance
Electronic Dance: 0.89Ambient: 0.05Pop: 0.04Show all
ElectroTranceHouse
Electro: 0.48Trance: 0.45House: 0.3Show all
EnergeticUplifting
Energetic: 0.92Uplifting: 0.87Happy: 0.5Show all
ConfidentEnergeticPowerfulShow all
Confident: 0.56Energetic: 0.55Powerful: 0.55Show all
Playful
Playful: 0.78Bold: 0.04Warm: 0.04Show all
Pulsing
Pulsing: 0.79Groovy: 0.42Bouncy: 0.32Show all
0.52
0.86
  High
Positive
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
contemporary
-
-
1gihuPhrLraKYrJMAEONyc
Listen on Spotify
|
Similarity""",
    """100 gecs x Laura Les x Dylan Brady - gec 2 Ü
85
C major
Female
  High
PopElectronic Dance
Pop: 0.76Electronic Dance: 0.45Rock: 0.12Show all
Electro
Electro: 0.44Breakbeat/Drum&Bass: 0.34Abstract IDM Leftfield: 0.26Show all
Energetic
Energetic: 0.72Happy: 0.52Uplifting: 0.49Show all
StrongConfidentEnergeticShow all
Strong: 0.53Confident: 0.49Energetic: 0.48Show all
PowerfulBoldUnpolishedShow all
Powerful: 0.43Bold: 0.38Unpolished: 0.32Show all
StompingBouncyDrivingShow all
Stomping: 0.37Bouncy: 0.36Driving: 0.35Show all
0.32
0.65
  High
Positive
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
mid / late 2000s
-
-
6oEpHl3cdz5s3gr2JVjok5
Listen on Spotify
|
Similarity""",
    """The Coup - The Guillotine
108
E minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.82RnB: 0.06Pop: 0.04Show all
GangstaPop-Rap
Gangsta: 0.65Pop-Rap: 0.58Jazzy Hip-Hop: 0.03Show all
AggressiveEnergeticUplifting
Energetic: 0.9Uplifting: 0.7Aggressive: 0.59Show all
PowerfulStrongResoluteShow all
Powerful: 0.64Strong: 0.63Resolute: 0.62Show all
BoldUnpolishedHeroicShow all
Bold: 0.7Unpolished: 0.46Heroic: 0.36Show all
StompingDriving
Stomping: 0.75Driving: 0.65Running: 0.2Show all
0.11
0.89
  High
Balanced
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
contemporary
-
-
0sAfPM3pfs0tdKwyGrwZHh
Listen on Spotify
|
Similarity""",
    """Bonnie Tyler - Holding Out for a Hero - From "Footloose" Soundtrack
150
A minor
Female
  High
Pop
Pop: 0.73Latin: 0.14Funk/Soul: 0.11Show all
-
-
EnergeticEpicUplifting
Energetic: 0.91Epic: 0.66Uplifting: 0.65Show all
BrightEuphoricUpbeatShow all
Bright: 0.5Euphoric: 0.49Upbeat: 0.48Show all
Heroic
Heroic: 0.54Powerful: 0.16Epic: 0.1Show all
DrivingSteadyRunning
Driving: 0.63Steady: 0.59Running: 0.57Show all
0.13
0.91
  High
Balanced
  Low
  Low
PercussionBass
Bass: ThroughoutPercussion: ThroughoutAcoustic Guitar: AbsentShow all
4/4
late 1970s / early 1980s
-
-
5Hyr47BBGpvOfcykSCcaw9
Listen on Spotify
|
Similarity""",
    """T-Mass - Ignoring My Heart
75
A minor
None
None
Electronic Dance
Electronic Dance: 0.88Ambient: 0.05Pop: 0.04Show all
Breakbeat/Drum&Bass
Breakbeat/Drum&Bass: 0.7Electro: 0.18Abstract IDM Leftfield: 0.12Show all
EnergeticUplifting
Energetic: 0.8Uplifting: 0.62Aggressive: 0.42Show all
ConfidentDeterminedPowerfulShow all
Confident: 0.6Determined: 0.54Powerful: 0.53Show all
BoldCoolPowerfulShow all
Bold: 0.47Cool: 0.39Powerful: 0.38Show all
RoboticDrivingRunningShow all
Robotic: 0.49Driving: 0.41Running: 0.37Show all
0.14
0.58
  High
Balanced
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
contemporary
-
-
3FbEzEjhvAu6hYbDViwMpt
Listen on Spotify
|
Similarity""",
    """Citizen - Jet
134
D major
Male
  High
RockMetal
Rock: 0.67Metal: 0.63Pop: 0.04Show all
Doom MetalIndie/Alternative
Indie/Alternative: 0.77Doom Metal: 0.72Heavy Metal: 0.26Show all
EnergeticUplifting
Energetic: 0.85Uplifting: 0.71Epic: 0.45Show all
ConfidentUpliftingResoluteShow all
Confident: 0.63Uplifting: 0.6Resolute: 0.59Show all
HeroicPowerful
Heroic: 0.49Powerful: 0.45Epic: 0.29Show all
DrivingRunningStomping
Driving: 0.59Running: 0.46Stomping: 0.35Show all
0.15
0.74
  High
Balanced
  Low
  Low
Bass GuitarElectric GuitarPercussionShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
late 2000s / contemporary
-
-
0QeR9qS8tqumgcjAFIwpTr
Listen on Spotify
|
Similarity
""",
    """Run The Jewels x El-P x Killer Mike x Zack De La Rocha x Pharrell Williams - JU$T (feat. Pharrell Williams & Zack de la Rocha)
133
Bb minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
GangstaPop-RapTrap
Trap: 0.49Gangsta: 0.33Pop-Rap: 0.31Show all
DarkEnergetic
Dark: 0.69Energetic: 0.56Aggressive: 0.42Show all
SeriousPonderousSpiritualShow all
Serious: 0.47Ponderous: 0.42Spiritual: 0.37Show all
Sparse
Sparse: 0.39Warm: 0.13Unpolished: 0.11Show all
Bouncy
Bouncy: 0.75Driving: 0.42Flowing: 0.26Show all
-0.45
0.52
  High
Negative
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
late 2000s / contemporary
-
-
10vS4ZLi4XWlIsNXSQXgqh
Listen on Spotify
|
Similarity""",
    """BLP KOSHER x BabyTron - Mazel Tron
180
B minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.82RnB: 0.06Pop: 0.04Show all
Trap
Trap: 0.71Pop-Rap: 0.24Gangsta: 0.21Show all
EnergeticUpliftingAggressive
Energetic: 0.8Uplifting: 0.66Aggressive: 0.6Show all
ConfidentResoluteDeterminedShow all
Confident: 0.7Resolute: 0.64Determined: 0.61Show all
BoldUnpolishedCoolShow all
Bold: 0.82Unpolished: 0.6Cool: 0.53Show all
Bouncy
Bouncy: 0.57Groovy: 0.39Driving: 0.27Show all
0.12
0.72
  High
Balanced
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
contemporary
-
-
5Ex5aIXLQimPjhiRUZjtre
Listen on Spotify
|
Similarity""",
    """Bring Me The Horizon - Teardrops
96
D minor
Male
  High
RockMetal
Rock: 0.65Metal: 0.43Pop: 0.18Show all
Hard RockIndie/AlternativeMetalcore
Indie/Alternative: 0.61Metalcore: 0.52Hard Rock: 0.46Show all
AggressiveDarkEnergeticShow all
Energetic: 0.89Aggressive: 0.62Epic: 0.61Show all
PowerfulStrongDeterminedShow all
Powerful: 0.67Strong: 0.61Determined: 0.58Show all
PowerfulEpicUnpolished
Powerful: 0.8Epic: 0.67Unpolished: 0.65Show all
DrivingRunningStomping
Driving: 0.73Running: 0.57Stomping: 0.37Show all
-0.51
0.86
  High
Negative
  Low
  Low
Bass GuitarElectric GuitarPercussionShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
contemporary
-
-
3aniWcwiiYKHpm3F5TdeKD
Listen on Spotify
|
Similarity""",
    """KT Tunstall - Suddenly I See
200
D major
Female
  High
PopRock
Pop: 0.78Rock: 0.58Latin: 0.16Show all
Folk RockIndie/AlternativePop Soft Rock
Pop Soft Rock: 0.67Folk Rock: 0.53Indie/Alternative: 0.36Show all
ChillHappy
Happy: 0.7Chill: 0.68Uplifting: 0.37Show all
BrightFeelGoodOptimisticShow all
Bright: 0.6Feel Good: 0.59Optimistic: 0.56Show all
Sparkling
Sparkling: 0.8Warm: 0.39Ethereal: 0.05Show all
DrivingRunningStompingShow all
Driving: 0.39Running: 0.31Stomping: 0.24Show all
0.68
0.12
Medium
Positive
  Low
  Low
Bass GuitarElectric GuitarPercussionShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
late 1990s / early 2000s
-
-
5p9XWUdvbUzmPCukOmwoU3
Listen on Spotify
|
Similarity"""]

songs = []
for songString in songsStrings:
    songs.append(SONG(songString))

songNames = []
bmps = []
keys = []
predominantVoiceGenders = []
genreTags = []
moodTags = []
characterTags = []
energyLevels = []
for song in songs:
    songNames.append(song.songName)
    bmps.append(song.bpm)
    keys.append(song.key)
    predominantVoiceGenders.append(song.predominantVoiceGender)
    genreTags.append(song.genreTags[0])
    moodTags.append(song.moodTags)
    characterTags.append(song.characterTags)
    energyLevel = song.energyLevel
    energyLevel = energyLevel.strip()
    print(energyLevel)
    if energyLevel == 'High':
        energyLevels.append(3)
    if energyLevel == 'Medium':
        energyLevels.append(2)
    if energyLevel == 'Low':
        energyLevels.append(1)

df = pd.DataFrame(list(zip(songNames, bmps, keys, predominantVoiceGenders,
                  genreTags, moodTags, characterTags, energyLevels)))
gfg_csv_data = df.to_csv('NicksSongStringProcessor/songData.csv', index=False)

nick = 5
