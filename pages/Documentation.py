import streamlit as st

st.set_page_config(layout="centered")
st.title("Documentation")

infile = open("pages/Documentation.md", "r")  
lines = infile.readlines()
st.markdown("".join(lines), unsafe_allow_html=True)