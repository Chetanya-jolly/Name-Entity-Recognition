"""
# This the file for deploying the name entity recognition code
"""

import streamlit as st
import pandas as pd
from ner import NER 

st.title("Name Entity Recognition")
st.write("Enter some text below and see the named entities detected.")

if "content" not in st.session_state:
    st.session_state.content = ""

st.session_state.content = st.text_area("Your text here:", st.session_state.content, height=150)

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Analyze"):
        if st.session_state.content.strip():
            df = NER(st.session_state.content)
            st.dataframe(df)
        else:
            st.warning("Please enter some text to analyze.")

with col2:
    if st.button("Reset"):
        st.session_state.content = ""
        st.experimental_rerun()  # Reset the input field