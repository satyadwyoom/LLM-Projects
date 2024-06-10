import os
import streamlit as st
import pandas as pd

from insights_generator.insights import generate_response

os.environ["OPENAI_API_KEY"] = ""

st.markdown("# Data Insight Generator <sub> by Satyadwyoom Kumar </sub>", unsafe_allow_html=True)
st.write("Upload a CSV file to generate your insights")
uploaded_file = st.file_uploader("Choose file", type="csv")
target_label = st.text_input("Choose target variable for which you need insights")


if st.button("Generate Insights"):

    if uploaded_file and target_label:
        df = pd.read_csv(uploaded_file)
        target = target_label


    with st.spinner("Generating...."):
        response = generate_response(df, target)
        st.success("Insights Generated!!")
        st.write(response)

