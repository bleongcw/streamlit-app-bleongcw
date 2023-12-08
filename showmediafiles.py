# Core Packages
import streamlit as st

# Working with Media Files/Videos/Images/Audio
from PIL import Image
img = Image.open("data/image_03.jpg")
st.image(img)

# Getting image from URL
st.image("https://www.analyse.asia/content/images/2023/01/AA_logo_colour2.png")

# Display Video
video_file = open("data/secret_of_success.mp4", "rb").read()
st.video(video_file)

# Display Audio

audio_file = open("data/song.mp3", "rb")
st.audio(audio_file.read())
