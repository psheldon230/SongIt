from song import SONG
import pandas as pd
songsStrings = ["""Bad Bunny - Tití Me Preguntó
111
F minor
Male
  High
Latin
Latin: 0.69Rap/Hip-Hop: 0.35Reggae: 0.18Show all
-
-
EnergeticSexyUplifting
Uplifting: 0.76Energetic: 0.71Sexy: 0.54Show all
CoolSeductiveSexyShow all
Cool: 0.41Seductive: 0.35Sexy: 0.35Show all
Luxurious
Luxurious: 0.79Sophisticated: 0.17Cool: 0.12Show all
Bouncy
Bouncy: 0.87Steady: 0.26Groovy: 0.22Show all
0.61
0.70
  High
Positive
  Low
  Low
PercussionSynthBass
Percussion: ThroughoutSynth: ThroughoutBass: FrequentlyShow all
4/4
contemporary
-
-
1IHWl5LamUGEuP4ozKQSXZ
Listen on Spotify
|
Similarity""","""Bad Bunny x Chencho Corleone - Me Porto Bonito
184
C# minor
Male
  High
Latin
Latin: 0.81Pop: 0.19Rap/Hip-Hop: 0.12Show all
-
-
ChillSexy
Chill: 0.65Sexy: 0.64Uplifting: 0.4Show all
CoolSexySeductiveShow all
Cool: 0.5Sexy: 0.48Seductive: 0.47Show all
Cool
Cool: 0.73Sophisticated: 0.38Warm: 0.29Show all
BouncySteady
Bouncy: 0.85Steady: 0.61Groovy: 0.17Show all
0.41
0.09
Medium
Positive
Medium
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
contemporary
-
-
6Sq7ltF9Qa7SNFBsV5Cogx
Listen on Spotify
|
Similarity""","""Beyoncé - Single Ladies (Put a Ring on It)
194
E major
Female
  High
RnBRap/Hip-HopFunk/SoulShow all
RnB: 0.67Rap/Hip-Hop: 0.55Funk/Soul: 0.49Show all
Contemporary RnBPop-Rap
Pop-Rap: 0.52Contemporary RnB: 0.34Gangsta: 0.06Show all
AggressiveEnergeticUplifting
Energetic: 0.86Uplifting: 0.61Aggressive: 0.56Show all
ConfidentEnergeticEuphoricShow all
Confident: 0.55Energetic: 0.53Euphoric: 0.52Show all
Powerful
Powerful: 0.59Sparkling: 0.36Bold: 0.31Show all
DrivingStompingRunning
Driving: 0.88Stomping: 0.75Running: 0.73Show all
0.02
0.86
  High
Balanced
  Low
  Low
PercussionBass
Bass: ThroughoutPercussion: ThroughoutAcoustic Guitar: AbsentShow all
4/4
contemporary
-
-
5mMjkxGijQB4JZallYrkOW
Listen on Spotify
|
Similarity""","""Beyoncé x JAY-Z - Crazy In Love (feat. Jay-Z)
99
D minor
Female
  High
Rap/Hip-HopFunk/SoulRnB
Rap/Hip-Hop: 0.55Funk/Soul: 0.52RnB: 0.41Show all
Contemporary RnBSoulPop-Rap
Contemporary RnB: 0.47Soul: 0.36Pop-Rap: 0.31Show all
EnergeticUpliftingHappy
Energetic: 0.85Uplifting: 0.84Happy: 0.59Show all
ConfidentPowerfulStrongShow all
Confident: 0.57Powerful: 0.55Strong: 0.54Show all
RetroLuxurious
Retro: 0.72Luxurious: 0.46Powerful: 0.24Show all
GroovySteady
Groovy: 0.85Steady: 0.7Bouncy: 0.35Show all
0.63
0.77
  High
Positive
  Low
  Low
Bass GuitarElectric GuitarPercussionShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
mid / late 1990s
-
-
0TwBtDAWpkpM3srywFVOV5
Listen on Spotify
|
Similarity""","""Jim Croce - Time in a Bottle
134
D major
Male
  High
Folk/Country
Folk/Country: 0.48Pop: 0.2Rock: 0.14Show all
Folk
Folk: 0.9Country: 0.12Blues Rock: 0Show all
CalmChillRomanticShow all
Chill: 0.9Romantic: 0.86Calm: 0.82Show all
WarmDreamyRomanticShow all
Warm: 0.57Dreamy: 0.54Romantic: 0.54Show all
Warm
Warm: 0.78Sparkling: 0.1Ethereal: 0.07Show all
FlowingSteady
Flowing: 0.66Steady: 0.51Bouncy: 0.12Show all
-0.09
-0.80
  Low
Balanced
  Low
  Low
Acoustic Guitar
Acoustic Guitar: ThroughoutBass: AbsentBass Guitar: AbsentShow all
3/4
early / mid 1970s
-
-
561F1zqRwGPCTMRsLsXVtL
Listen on Spotify
|
Similarity""", """Jim Croce - I Got a Name - Stereo Version
174
E major
Male
  High
Rock
Rock: 0.71Blues: 0.39Pop: 0.15Show all
Folk RockPop Soft Rock
Folk Rock: 0.6Pop Soft Rock: 0.55Blues Rock: 0.23Show all
Ambiguous
Epic: 0.49Romantic: 0.49Happy: 0.47Show all
EmotionalSolemnHopefulShow all
Emotional: 0.52Solemn: 0.5Hopeful: 0.49Show all
SparklingWarm
Sparkling: 0.59Warm: 0.49Ethereal: 0.09Show all
DrivingStomping
Driving: 0.47Stomping: 0.34Running: 0.19Show all
0.16
0.17
Medium
Balanced
  Low
  Low
PianoStringsAcoustic Guitar
Acoustic Guitar: ThroughoutPiano: ThroughoutStrings: ThroughoutShow all
4/4
late 1970s / early 1980s
-
-
38llcrfX1arUqrEe0DRRzW
Listen on Spotify
|
Similarity""","""Jim Croce - I'll Have To Say I Love You In A Song
134
A major
Male
  High
Folk/Country
Folk/Country: 0.51Pop: 0.09Rock: 0.09Show all
Country
Country: 0.75Folk: 0.25Blues Rock: 0Show all
CalmChillRomanticShow all
Chill: 0.92Calm: 0.8Romantic: 0.73Show all
WarmRomanticDreamyShow all
Warm: 0.58Romantic: 0.54Dreamy: 0.53Show all
SparklingWarm
Sparkling: 0.81Warm: 0.5Ethereal: 0.06Show all
BouncyFlowing
Bouncy: 0.54Flowing: 0.51Pulsing: 0.11Show all
-0.25
-0.77
  Low
Balanced
  Low
  Low
PercussionStringsAcoustic GuitarShow all
Acoustic Guitar: ThroughoutBass Guitar: ThroughoutPercussion: ThroughoutShow all
4/4
early / mid 1970s
-
-
4t8tx6o7oM6Ax66ZUU361y
Listen on Spotify
|
Similarity
""","""Jim Croce - New York's Not My Home
133
E major
Male
  High
RockPop
Rock: 0.51Pop: 0.38Folk/Country: 0.25Show all
Pop Soft RockFolk RockPsychedelic Progressive Rock
Psychedelic Progressive Rock: 0.42Pop Soft Rock: 0.41Folk Rock: 0.4Show all
CalmChillRomanticShow all
Chill: 0.91Romantic: 0.87Calm: 0.86Show all
RelaxedKindWarmShow all
Relaxed: 0.52Kind: 0.51Warm: 0.51Show all
RetroWarm
Retro: 0.82Warm: 0.06Cool: 0.04Show all
Bouncy
Bouncy: 0.47Flowing: 0.26Groovy: 0.2Show all
-0.13
-0.84
  Low
Balanced
  Low
  Low
Bass GuitarPercussionPianoShow all
Acoustic Guitar: ThroughoutBass Guitar: ThroughoutPercussion: ThroughoutShow all
4/4
mid / late 1970s
-
-
2iAe3yqQ5QYX8SI1iF4kJ6
Listen on Spotify
|
Similarity""","""Queen - Bohemian Rhapsody - 2011 Mix
141
Eb major
Female
  High
RockBlues
Rock: 0.6Blues: 0.43Metal: 0.06Show all
Blues RockHard Rock
Blues Rock: 0.6Hard Rock: 0.46Psychedelic Progressive Rock: 0.13Show all
EnergeticEpic
Epic: 0.75Energetic: 0.53Sad: 0.43Show all
SeriousEmotionalConcernedShow all
Emotional: 0.52Serious: 0.52Concerned: 0.51Show all
RetroPowerfulUnpolished
Retro: 0.7Powerful: 0.63Unpolished: 0.49Show all
Stomping
Stomping: 0.75Driving: 0.09Steady: 0.09Show all
-0.43
0.45
  High
Negative
  Low
  Low
Bass GuitarElectric GuitarPercussionShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
mid / late 1990s
-
-
3z8h0TU7ReDPLIbEnYhWZb
Listen on Spotify
|
Similarity""","""Queen - Killer Queen - 2011 Mix
115
C minor
None
None
Blues
Blues: 0.56Rock: 0.29Funk/Soul: 0.05Show all
-
-
EnergeticHappyUplifting
Happy: 0.72Energetic: 0.71Uplifting: 0.65Show all
BrightFeelGoodCheerfulShow all
Bright: 0.64Feel Good: 0.63Cheerful: 0.61Show all
RetroBoldUnpolished
Retro: 0.61Bold: 0.44Unpolished: 0.43Show all
StompingSteady
Stomping: 0.56Steady: 0.51Driving: 0.21Show all
0.64
0.68
  High
Positive
  Low
  Low
BassBass GuitarElectric GuitarShow all
Acoustic Guitar: ThroughoutBass: ThroughoutBass Guitar: ThroughoutShow all
4/4
late 1970s / early 1980s
-
-
300YN8ebGB90nDuzgz0f3O
Listen on Spotify
|
Similarity""","""Billy Joel - Piano Man
180
C major
Male
  High
Folk/CountryRock
Folk/Country: 0.45Rock: 0.41Singer/Songwriters: 0.15Show all
CountryFolk Rock
Folk Rock: 0.58Country: 0.51Folk: 0.49Show all
HappyRomantic
Romantic: 0.58Happy: 0.51Chill: 0.46Show all
RomanticSolemnSentimentalShow all
Romantic: 0.51Solemn: 0.5Sentimental: 0.49Show all
RetroWarm
Retro: 0.87Warm: 0.05Playful: 0.03Show all
BouncyFlowingStomping
Bouncy: 0.41Flowing: 0.31Stomping: 0.26Show all
0.16
0.02
Medium
Balanced
  Low
  Low
PercussionPianoAcoustic GuitarShow all
Acoustic Guitar: ThroughoutBass Guitar: ThroughoutPercussion: ThroughoutShow all
3/4
mid / late 1970s
-
-
70C4NyhjD5OZUMzvWZ3njJ
Listen on Spotify
|
Similarity""","""Billy Joel - She's Got a Way
73
F# major
Male
  High
RockPopSinger/SongwritersShow all
Rock: 0.47Pop: 0.38Singer/Songwriters: 0.36Show all
Pop Soft Rock
Pop Soft Rock: 0.6Blues Rock: 0.43Folk Rock: 0.31Show all
RomanticChillHappy
Romantic: 0.84Chill: 0.66Happy: 0.53Show all
SentimentalRomanticWarmShow all
Sentimental: 0.7Romantic: 0.63Warm: 0.63Show all
WarmSparklingSophisticated
Warm: 0.65Sparkling: 0.54Sophisticated: 0.45Show all
FlowingSteady
Flowing: 0.64Steady: 0.48Stomping: 0.17Show all
0.42
-0.23
Medium
Positive
  Low
  Low
PianoStrings
Piano: ThroughoutStrings: ThroughoutAcoustic Guitar: AbsentShow all
4/4
late 1970s / early 1980s
-
-
3Ie2eLOIj2IhKnzPwXrLbJ
Listen on Spotify
|
Similarity""","""Billy Joel - Vienna
126
Bb major
Male
  High
PopRockSinger/SongwritersShow all
Pop: 0.62Rock: 0.58Singer/Songwriters: 0.38Show all
Pop Soft Rock
Pop Soft Rock: 0.71Folk Rock: 0.3Blues Rock: 0.24Show all
CalmChillRomanticShow all
Chill: 0.92Romantic: 0.81Calm: 0.73Show all
RomanticSentimentalNostalgicShow all
Romantic: 0.52Sentimental: 0.52Nostalgic: 0.51Show all
Warm
Warm: 0.79Sophisticated: 0.1Playful: 0.07Show all
Flowing
Flowing: 0.82Steady: 0.09Pulsing: 0.07Show all
0.28
-0.70
  Low
Balanced
  Low
  Low
PercussionPianoBass
Bass: ThroughoutPercussion: ThroughoutPiano: ThroughoutShow all
4/4
mid / late 1980s
-
-
4U45aEWtQhrm8A5mxPaFZ7
Listen on Spotify
|
Similarity""","""Billy Joel - Scenes from an Italian Restaurant
99
C major
Male
  High
Rock
Rock: 0.69Pop: 0.26Folk/Country: 0.17Show all
Blues Rock
Blues Rock: 0.52Pop Soft Rock: 0.31Folk Rock: 0.26Show all
EnergeticHappyUplifting
Uplifting: 0.85Energetic: 0.84Happy: 0.67Show all
BrightUpbeatFeelGoodShow all
Bright: 0.59Upbeat: 0.58Feel Good: 0.57Show all
RetroPowerfulWarm
Retro: 0.87Powerful: 0.04Warm: 0.04Show all
Groovy
Groovy: 0.61Bouncy: 0.39Driving: 0.32Show all
0.66
0.75
  High
Positive
  Low
  Low
Bass GuitarElectric GuitarPercussionShow all
Bass: ThroughoutBass Guitar: ThroughoutElectric Guitar: ThroughoutShow all
4/4
mid / late 1970s
-
-
3utq2FgD1pkmIoaWfjXWAU
Listen on Spotify
|
Similarity""","""Billy Joel - Uptown Girl
129
B minor
Male
  High
Pop
Pop: 0.67Electronic Dance: 0.4Funk/Soul: 0.33Show all
-
-
EnergeticUpliftingHappy
Energetic: 0.82Uplifting: 0.79Happy: 0.69Show all
BrightFeelGoodCheerfulShow all
Bright: 0.65Feel Good: 0.64Cheerful: 0.63Show all
CoolSparkling
Cool: 0.54Sparkling: 0.39Retro: 0.15Show all
StompingDriving
Stomping: 0.73Driving: 0.68Running: 0.2Show all
0.67
0.74
  High
Positive
  Low
  Low
PercussionBassBass Guitar
Bass: ThroughoutBass Guitar: ThroughoutPercussion: ThroughoutShow all
4/4
early / mid 1980s
-
-
5zA8vzDGqPl2AzZkEYQGKh
Listen on Spotify
|
Similarity""","""Cardi B x Bad Bunny x J Balvin - I Like It
136
F minor
Female
  High
PopLatinRap/Hip-Hop
Pop: 0.57Latin: 0.5Rap/Hip-Hop: 0.37Show all
-
-
EnergeticSexyHappyShow all
Uplifting: 0.87Energetic: 0.8Sexy: 0.6Show all
ConfidentPowerfulStrongShow all
Confident: 0.59Powerful: 0.59Strong: 0.58Show all
Luxurious
Luxurious: 0.63Cool: 0.26Bold: 0.21Show all
Bouncy
Bouncy: 0.88Groovy: 0.45Driving: 0.11Show all
0.65
0.76
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
58q2HKrzhC3ozto2nDdN4z
Listen on Spotify
|
Similarity""","""Polo G - Through Da Storm
149
D minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
Trap
Trap: 0.92Pop-Rap: 0.16Gangsta: 0.02Show all
CalmChillEthereal
Chill: 0.88Calm: 0.62Ethereal: 0.61Show all
ConfidentMotivationalAnthemicShow all
Confident: 0.61Motivational: 0.55Anthemic: 0.52Show all
Cool
Cool: 0.71Bold: 0.22Unpolished: 0.09Show all
Groovy
Groovy: 0.82Driving: 0.18Pulsing: 0.15Show all
-0.20
-0.58
  Low
Balanced
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
mid / late 2000s
-
-
3NqCEpT8xsHdzpiRlM1kpS
Listen on Spotify
|
Similarity""","""Young Thug x Future - Relationship (feat. Future)
146
G major
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
Trap
Trap: 0.81Pop-Rap: 0.14Gangsta: 0.1Show all
ChillDark
Chill: 0.61Dark: 0.57Ethereal: 0.44Show all
ConfidentResoluteStrongShow all
Confident: 0.61Resolute: 0.52Strong: 0.52Show all
CoolLuxurious
Cool: 0.77Luxurious: 0.49Bold: 0.16Show all
DrivingBouncyStomping
Driving: 0.63Bouncy: 0.45Stomping: 0.42Show all
-0.29
-0.13
Medium
Balanced
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
contemporary
-
-
25oOaleife6E2MIKmFkPvg
Listen on Spotify
|
Similarity
""","""Chance the Rapper - Same Drugs
180
F# major
Male
  High
Pop
Pop: 0.74RnB: 0.42Rap/Hip-Hop: 0.4Show all
-
-
ChillHappyRomantic
Chill: 0.89Happy: 0.62Romantic: 0.58Show all
EmotionalPassionateSeriousShow all
Emotional: 0.53Passionate: 0.51Serious: 0.51Show all
RetroWarmPlayful
Retro: 0.38Warm: 0.08Playful: 0.07Show all
Flowing
Flowing: 0.65Bouncy: 0.21Groovy: 0.18Show all
0.59
-0.37
  Low
Positive
  Low
  Low
Piano
Piano: ThroughoutAcoustic Guitar: AbsentBass: AbsentShow all
4/4
late 1990s / early 2000s
-
-
6m9qPYXmhge2QhBLfFKnVF
Listen on Spotify
|
Similarity""","""Chance the Rapper x Knox Fortune - All Night (feat. Knox Fortune)
112
B minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
Pop-Rap
Pop-Rap: 0.63Gangsta: 0.22Contemporary RnB: 0.11Show all
EnergeticUplifting
Energetic: 0.81Uplifting: 0.73Happy: 0.35Show all
OptimisticCoolHopefulShow all
Optimistic: 0.42Cool: 0.39Hopeful: 0.38Show all
Cool
Cool: 0.69Warm: 0.12Luxurious: 0.11Show all
DrivingPulsingBouncyShow all
Driving: 0.73Pulsing: 0.53Bouncy: 0.52Show all
0.50
0.80
  High
Positive
  Low
  Low
PercussionBass
Bass: ThroughoutPercussion: ThroughoutAcoustic Guitar: AbsentShow all
4/4
early / mid 2000s
-
-
60xaS8mYBKUW4VQQ666N0T
Listen on Spotify
|
Similarity""","""Brandon. - Smoke Break Freestyle
75
F# minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
Pop-RapTrap
Trap: 0.73Pop-Rap: 0.42Gangsta: 0.03Show all
SexyAggressiveEnergetic
Sexy: 0.44Aggressive: 0.43Energetic: 0.43Show all
SeriousSeductivePassionateShow all
Serious: 0.55Seductive: 0.54Passionate: 0.51Show all
CoolUnpolishedBoldShow all
Cool: 0.5Unpolished: 0.44Bold: 0.35Show all
Bouncy
Bouncy: 0.59Groovy: 0.25Flowing: 0.23Show all
0.15
0.27
Medium
Balanced
  Low
  Low
Bass GuitarPercussionSynthShow all
Bass: ThroughoutBass Guitar: ThroughoutPercussion: ThroughoutShow all
4/4
contemporary
-
-
1M8H3jwMRRRMmXZyCYuZQo
Listen on Spotify
|
Similarity""","""Polo G x Lil Baby - Be Something (feat. Lil Baby)
136
G minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
Trap
Trap: 0.85Gangsta: 0.12Pop-Rap: 0.09Show all
CalmChillEtherealShow all
Chill: 0.9Ethereal: 0.75Calm: 0.69Show all
SeriousDeterminedPassionateShow all
Serious: 0.48Determined: 0.47Passionate: 0.46Show all
BoldCoolUnpolishedShow all
Bold: 0.47Cool: 0.46Unpolished: 0.38Show all
Bouncy
Bouncy: 0.84Driving: 0.16Groovy: 0.16Show all
-0.28
-0.64
  Low
Balanced
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
late 2000s / contemporary
-
-
65jw6GhwQW3Db55PxlPEpS
Listen on Spotify
|
Similarity
""","""Polo G - Dyin Breed
160
C major
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
Trap
Trap: 0.87Pop-Rap: 0.24Gangsta: 0.08Show all
Chill
Chill: 0.59Sexy: 0.47Ethereal: 0.41Show all
ConfidentUpbeatEuphoricShow all
Confident: 0.54Upbeat: 0.51Euphoric: 0.51Show all
CoolBoldUnpolished
Cool: 0.7Bold: 0.61Unpolished: 0.55Show all
BouncyDriving
Bouncy: 0.56Driving: 0.54Groovy: 0.31Show all
0.05
0.03
Medium
Balanced
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
contemporary
-
-
2bGEPdcL80FFHQ3VxcYBJQ
Listen on Spotify
|
Similarity""","""Polo G - Martin & Gina
94
C# minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
Trap
Trap: 0.76Pop-Rap: 0.4Gangsta: 0.09Show all
Chill
Chill: 0.87Calm: 0.48Ethereal: 0.48Show all
OptimisticFeelGoodConfidentShow all
Feel Good: 0.51Optimistic: 0.51Confident: 0.5Show all
BoldHeroic
Bold: 0.4Heroic: 0.39Cool: 0.19Show all
Groovy
Groovy: 0.88Bouncy: 0.38Flowing: 0.26Show all
0.13
-0.42
  Low
Balanced
  Low
  Low
PercussionBassBass Guitar
Bass: ThroughoutBass Guitar: ThroughoutPercussion: ThroughoutShow all
4/4
contemporary
-
-
1VLtjHwRWOVJiE5Py7JxoQ
Listen on Spotify
|
Similarity""","""Polo G - Don't Believe The Hype
160
Bb minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
Pop-RapTrap
Trap: 0.66Pop-Rap: 0.54Gangsta: 0.12Show all
EnergeticUpliftingAggressive
Energetic: 0.45Uplifting: 0.41Aggressive: 0.38Show all
PassionateSeriousConfidentShow all
Passionate: 0.57Serious: 0.55Confident: 0.53Show all
CoolBoldUnpolished
Cool: 0.66Bold: 0.6Unpolished: 0.47Show all
GroovyFlowingBouncy
Groovy: 0.33Flowing: 0.29Bouncy: 0.28Show all
0.00
0.26
Medium
Balanced
  Low
  Low
PercussionSynthBass
Bass: ThroughoutPercussion: ThroughoutSynth: ThroughoutShow all
4/4
contemporary
-
-
3TciLI5wo7RddPtAFhiU9V
Listen on Spotify
|
Similarity""","""Gunna x Lil Uzi Vert - RELENTLESS (feat. Lil Uzi Vert)
115
F# minor
Male
  High
Rap/Hip-Hop
Rap/Hip-Hop: 0.83RnB: 0.06Pop: 0.04Show all
Pop-RapTrap
Trap: 0.7Pop-Rap: 0.47Gangsta: 0.06Show all
DarkEnergetic
Dark: 0.71Energetic: 0.47Ethereal: 0.46Show all
ConfidentResolutePowerfulShow all
Confident: 0.62Resolute: 0.6Powerful: 0.59Show all
BoldUnpolishedPowerful
Bold: 0.84Unpolished: 0.65Powerful: 0.54Show all
Bouncy
Bouncy: 0.48Robotic: 0.31Driving: 0.29Show all
-0.49
0.43
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
6nDSLDomNqfet6w0r1GHAz
Listen on Spotify
|
Similarity
""","""Billy Joel - Honesty
134
G minor
Female
  High
Folk/CountryPopRockShow all
Folk/Country: 0.34Pop: 0.24Rock: 0.23Show all
Country
Country: 0.9Folk: 0.12Blues Rock: 0Show all
CalmChillRomanticShow all
Chill: 0.89Calm: 0.78Romantic: 0.7Show all
SolemnRomanticBittersweetShow all
Solemn: 0.5Romantic: 0.49Bittersweet: 0.43Show all
WarmRetro
Warm: 0.67Retro: 0.65Sparkling: 0.1Show all
Steady
Steady: 0.85Flowing: 0.11Groovy: 0.11Show all
-0.29
-0.75
  Low
Balanced
  Low
  Low
BassBass GuitarElectric GuitarShow all
Acoustic Guitar: ThroughoutBass: ThroughoutBass Guitar: ThroughoutShow all
4/4
mid / late 1970s
-
-
34E0Higz6fFVXlbVsn6TIW
Listen on Spotify
|
Similarity""","""Billy Joel - She's Always a Woman
178
Eb major
Male
  High
RockSinger/SongwritersPop
Rock: 0.73Singer/Songwriters: 0.61Pop: 0.49Show all
CountryFolk RockPop Soft Rock
Pop Soft Rock: 0.67Country: 0.59Folk Rock: 0.5Show all
CalmChillRomanticShow all
Chill: 0.92Calm: 0.9Romantic: 0.78Show all
WarmDreamyRomanticShow all
Warm: 0.56Dreamy: 0.54Romantic: 0.54Show all
Sparkling
Sparkling: 0.58Epic: 0.12Warm: 0.11Show all
Flowing
Flowing: 0.87Steady: 0.2Pulsing: 0.07Show all
-0.50
-0.87
  Low
Negative
  Low
  Low
Acoustic GuitarBassBass Guitar
Acoustic Guitar: ThroughoutBass: ThroughoutBass Guitar: ThroughoutShow all
3/4
mid / late 1970s
-
-
5RgFlk1fcClZd0Y4SGYhqH
Listen on Spotify
|
Similarity"""
]

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
