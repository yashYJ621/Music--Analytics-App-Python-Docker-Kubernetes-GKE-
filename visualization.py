# visualization.py
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import plotly.express as px

def display_data(df):

    key_mapping = {
        0: "C",
        1: "C#",
        2: "D",
        3: "D#",
        4: "E",
        5: "F",
        6: "F#",
        7: "G",
        8: "G#",
        9: "A",
        10: "A#",
        11: "B"
    }

    df["key_name"] = df["key"].map(key_mapping)

    df["key_mode"] = df["mode"].map({0: "Minor", 1: "Major"})
    
    
    st.subheader("Playlist Explorer")
    st.write(f"Number of Songs: {len(df)}")
    st.write(f"Total Duration: {convert_ms_to_min_sec(df['duration_ms'].sum())}")
    
    
    selected_columns = ["artist_name", "album_name", "song_name", "key_name", "key_mode", "popularity", "danceability", "energy", "loudness", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo"]

    st.subheader("Tracks & Their Features")
    st.write(df[selected_columns])
    
    st.subheader("Top Artists by number of songs in the Playlist")               
    # Group data by artist_name and concatenate song names into a single string
            
    # Group data by artist_name and concatenate song names into a single string
    top_artists = df.groupby("artist_name").agg({"song_name": list, "popularity": "mean"}).reset_index()
    top_artists["count"] = top_artists["song_name"].apply(len)

    # Sort artists by count in descending order and select top 10
    top_artists = top_artists.sort_values("count", ascending=False).head(5)

    # Create a DataFrame to explode the song names into separate rows
    top_songs = top_artists.explode("song_name")

    # Create an Altair stacked bar chart with text marks for popularity
    chart = (
        alt.Chart(top_songs).mark_bar().encode(
            y=alt.Y("popularity:Q", title="Popularity"),
            x=alt.X("artist_name:N", title="Artist Name"),
            color=alt.Color("song_name:N", title="Song Name"),
            tooltip=["artist_name", "song_name", alt.Tooltip("count()", title="Number of Songs"), alt.Tooltip("popularity:Q", title="Popularity")],
            text=alt.Text("popularity:Q", format=".1f")
        )
        .properties(height=600)
        .interactive()
    )

    # Display the chart
    st.altair_chart(chart, use_container_width=True)

    st.subheader("Top Songs by Popularity in this Playlist")

   
        
    # Group data by artist_name and select the song with the highest popularity
    top_artists = df.groupby("artist_name").agg({"song_name": "first", "popularity": "max"}).reset_index()

    # Sort artists by popularity in descending order and select top 10
    top_artists = top_artists.sort_values("popularity", ascending=False).head(10)

    # Create an Altair bar chart
    chart = (
        alt.Chart(top_artists).mark_bar().encode(
            x=alt.X("popularity:Q", title="Popularity"),
            y=alt.Y("artist_name:N", title="Artist Name"),
            color=alt.Color("popularity:Q", scale=alt.Scale(scheme="viridis"), title="Popularity"),
            tooltip=["artist_name", "song_name", "popularity"]
        )
        .properties(width=600)
        .interactive()
    )

    # Display the chart
    st.altair_chart(chart, use_container_width=True)

    st.subheader("Song Popularity Distribution")
    popularity_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("popularity:Q", bin=alt.Bin(maxbins=20), title="Popularity"),
        y="count()",
        tooltip="count()"
    ).properties(
        width=800,
        height=400
    )
    st.altair_chart(popularity_chart, use_container_width=True)
