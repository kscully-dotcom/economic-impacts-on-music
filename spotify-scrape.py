import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import sys
import time
import json

df = pd.read_csv('billboard-df.csv')
df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
df.sort_values(by=['date', 'track_rank'], inplace=True)
tracks = [df['track_title']]

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='177256dfab10424884575e3cee8126f4', 
    client_secret='24a3e2fa5bdb410591512b711754538c'))

results = sp.search(q=tracks, limit=5)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'], track['id'])
