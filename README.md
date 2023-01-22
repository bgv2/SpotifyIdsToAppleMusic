# SpotifyIdsToAppleMusic
This script takes in a Spotify URI for a track from a variable, looks up the track's info from the [Spotify API](https://developer.spotify.com/documentation/web-api/), then searches for it on Apple Music using the [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/Searching.html#//apple_ref/doc/uid/TP40017632-CH5-SW1). It then opens that track in the Mac's Music app.
## How to Use
1. Git clone this repo or download the ZIP
2. Run `pip install -r requirements.txt` in the same folder as this code (or just install the modules in `requirements.txt` manually)
3. Create a `tokens.toml` file and add this in there:
```toml
client_id="123my456clientid789"
client_secret="123my456secret789"
```
replacing the stuff in the quotes with your [Spotify API](https://developer.spotify.com/dashboard/) credentials. (No credentials are needed for the iTunes Search API.)

4. Change the Spotify URI in the variable at the top of the Python file.

5. Run the Python file.
## Check all matches before using them
This script is really basic, and it has no way of knowing if the track found on Apple Music is the same as the Spotify track. Ideally, it would check stuff like the music's duration and explicitness between the two to make sure it's the same song (but track names sometimes differ between the two services despite being the same song).
