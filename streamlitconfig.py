#Core Packages
import streamlit as st 
from PIL import Image 
img = Image.open("data/image_03.jpg")

# Method 1: Must be first activity of streamlit 
#st.set_page_config(page_title='Dorje Automation', page_icon='img', layout='wide', initial_sidebar_state='expanded')

# Method 2: Dictionary
PAGE_CONFIG = {"page_title":"Dorje Automation", "page_icon":":smiley", "layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

#Additional Packages

#Fxns

def main():
    st.title("Hello Streamlit Lovers🔥")
    st.sidebar.success("Menu")

if __name__ == '__main__':
    main()