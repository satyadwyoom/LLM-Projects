import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8080/essay/invoke",
                             json={"input":{"topic":input_text}})
    
    return response.json()['output']['content']


def get_llm_response(input_text):
    response = requests.post("http://localhost:8080/poem/invoke",
                             json={"input":{"topic":input_text}})
    
    return response.json()['output']


st.title('test gpt and llama')
input_text = st.text_input("OpenAI input: Ask any question")
input_text1 = st.text_input("llama3 input: Ask any question")


if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_llm_response(input_text1))
