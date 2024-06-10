from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms.ollama import Ollama

os.environ["OPENAI_API_KEY"] = ""

app = FastAPI(title="Langchain server test",
              version="1.0",
              description="simple chatbot")


add_routes(app,
           ChatOpenAI(),
           path='/openai')

model = ChatOpenAI()
llm = Ollama(model="llama3")

prompt1 = ChatPromptTemplate.from_template("{topic}")
prompt2 = ChatPromptTemplate.from_template("{topic}")

add_routes(app,
           prompt1|model,
           path="/essay")

add_routes(app,
           prompt2|llm,
           path="/poem")


if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8080)
    

