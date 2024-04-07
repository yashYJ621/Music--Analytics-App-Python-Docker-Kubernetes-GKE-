# spotify_functions.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import streamlit as st

# Spotipy credentials
client_id = "your_spotify_API_client_id"
client_secret = "your_spotify_API_client_secret"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def extract_data(playlist_uri):
    return sp.playlist_tracks(playlist_uri)

def transform_data(playlist_data):
    song_data = []
    for item in playlist_data['items']:
        track = item['track']
        artist = track['artists'][0]
        song_data.append({
            'song_id': track['id'],
            'song_name': track['name'],
            'artist_id': artist['id'],
            'artist_name': artist['name'],
            'duration_ms': track['duration_ms'],
            'popularity': track['popularity'],
            'url': track['external_urls']['spotify'],
            'album_id': track['album']['id'],
            'album_name': track['album']['name']
        })

    return pd.DataFrame(song_data)

#@st.cache_data
def get_audio_features(df):
    audio_features_data = []
    for song_id in df['song_id']:
        audio_features = sp.audio_features(song_id)
        audio_features_data.append(audio_features[0])

    audio_features_df = pd.DataFrame(audio_features_data)

    # Drop columns that are present in both DataFrames
    columns_to_drop = set(df.columns).intersection(set(audio_features_df.columns))
    df = df.drop(columns=columns_to_drop)

    # Merge audio features DataFrame with original DataFrame
    return pd.concat([df, audio_features_df], axis=1)
