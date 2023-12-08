# Basics and Fundamentals
# Core Packages
import streamlit as st

# Load EDA Packages
import pandas as pd 

# Display Data
df = pd.read_csv("iris.csv")

# Method 1
#st.dataframe(df)

# Adding a color style from pandas
#st.dataframe(df.style.highlight_max(axis=0))

# Method 2
#st.table(df)

# Method 3
#st.write(df.head())

# Display in JSON 
st.json({'data':'name'})

# Display in Code
mycode = """
def sayhello()
    print("Hello Streamlit Loves")

"""
st.code(mycode,language='python')
