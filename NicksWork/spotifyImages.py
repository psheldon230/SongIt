import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


class SPOTIFYINTERFACE:
    def __init__(self) -> None:

        self.CLIENT_ID = '74f5a95b1a994fd68caae2ac1baf6995'
        self.CLIENT_SECRET = '10d1617ce17f45dbbc1a577afeed9823'
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.CLIENT_ID,
                                                            client_secret=self.CLIENT_SECRET,
                                                            redirect_uri="http://localhost:8888/callback",
                                                            scope="user-library-read"
                                                            ))

    def searchAlbumCover300(self, searchStr="changes shrek 2"):
        searchResults = self.sp.search(
            searchStr, 1, 0, "track")
        track = searchResults['tracks']['items'][0]
        album = track['album']
        images = album['images']
        albumCover300URL = images[1]['url']
        return albumCover300URL
