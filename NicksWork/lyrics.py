from musixmatch import Musixmatch

musixmatch = Musixmatch("3dd66d658731d6c8be7a4d9b490b9f3f")

# x = musixmatch.track_search(q_track='Dior', q_artist='Pop Smoke', page_size=1, page=1, s_track_rating='desc')

# id = x['message']['body']['track_list'][0]['track']['track_id']

def FindLyrics(Song, Artist):
    lyrics_json = musixmatch.matcher_lyrics_get(Song, Artist)

    status = lyrics_json['message']['header']['status_code']

    if status != 200: return "Sorry, no lyrics available for this song"

    raw_lyrics = lyrics_json['message']['body']['lyrics']['lyrics_body']

    # Remove ellipsis
    lyrics_without_ellipsis = raw_lyrics.replace("...", "")
    
    # Remove disclaimer at end of lyrics
    lyrics_without_disclaimer = lyrics_without_ellipsis.split("*******")[0]
    
    return lyrics_without_disclaimer.strip()

# print(FindLyrics("i hate it here", "33kiro x Sukoyomi x p4rkr"))
# print(FindLyrics("Hello", "Adele"))