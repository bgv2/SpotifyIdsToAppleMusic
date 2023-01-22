import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import os
import tomllib
# try:
creds = None
with open("tokens.toml", "rb") as f:
    data = tomllib.load(f)
    creds = SpotifyClientCredentials(client_id=data["client_id"],
                                     client_secret=data["client_secret"])
sp = spotipy.Spotify(auth_manager=creds)

# ! change this to the Spotify uri for the track you want to search
trackUri = "spotify:track:abcdefg1234"

spotifyTrack = sp.track(trackUri)
print(" ".join((spotifyTrack["name"], "🅴 " if (
    spotifyTrack["explicit"] == True) else " ", spotifyTrack["external_urls"]["spotify"])))

iTunesResults = requests.get("https://itunes.apple.com/search", params={
    "term": " ".join((spotifyTrack["name"], spotifyTrack["album"]["name"])), # TODO: make this lookup one artist instead of the album name, so that it doesn't look up names of singles twice
    "entity": "song",
    "explicit": "No" if (spotifyTrack["explicit"] == False) else "Yes"
}).json()
iTunesTrack = iTunesResults["results"][0]
# ! The iTunes track may not be the same as the spotify track
# ! make sure to check the duration, the title, the artists, explicit/clean, etc
# ! for a more certain match
print(" ".join((iTunesTrack["trackName"], "🅴 " if (
    iTunesTrack["contentAdvisoryRating"] == "Explicit") else " ", iTunesTrack["trackViewUrl"])))
print(iTunesTrack["trackViewUrl"])

# opens the track in the Music app
os.system("open -a Music " +
          iTunesTrack["trackViewUrl"].replace("https://", "musics://", 1))
# except json.JSONDecodeError as e:
#     print("Delete the .cache file and run this again.\n")
#     print(e)
#     print(e.doc)
