from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "simple-testbot"

### prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to user queries"),
        ("user", "Question: {question}")
    ]
)


### Streamlit framework
st.title("LangChain Demo with LLama3 API")
input_text = st.text_input("Search the topic you want")


### openai

# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))