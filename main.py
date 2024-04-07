# main.py
import streamlit as st
import pandas as pd
from spotify_functions import extract_data, get_audio_features, transform_data
from visualizations import display_data


st.set_page_config(layout="wide")

def main():
    st.title("Spotify Playlist Analysis")
    playlist_link = st.text_input("Enter Spotify Playlist Link:")
    if st.button("Extract Data"):
        try:
            playlist_uri = playlist_link.split("/")[-1].split("?")[0]
            playlist_data = extract_data(playlist_uri)
            st.success("Playlist data extracted successfully.")
            df = transform_data(playlist_data)
            df_with_audio_features = get_audio_features(df)
            display_data(df_with_audio_features)
        except Exception as e:
            st.error(f"Error extracting playlist data: {e}")

if __name__ == "__main__":
    main()
