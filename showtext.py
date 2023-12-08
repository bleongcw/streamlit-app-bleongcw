# Basics and fundamentals
# Core Packages
import streamlit as st

# Working with and Displaying Text
st.text("Hello World this is")
name = "Bernard"
st.text("This is so {}".format(name))

# Header
st.header("Biography")

# Subheader
st.subheader("This is a subheader")

# Title
st.title("This is a title")

# Markdown
st.markdown("## This is a markdown")

# Displaying colored text/boostrap alert
st.success("Successful")
st.warning("This is danger")
st.info("This is information")
st.error("This is an error")
st.exception("This is an exception")

# Superfunction
st.write("Normal")
st.write("## This is a markdown text")
st.write(1+2)
st.write(dir(st))

#Help Info
st.help(range)