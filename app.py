
#LANGCHAIN_API_KEY"=" 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"
#GROQ_API_KEY"="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"
#langchain_project="chatbot"


from langchain_groq import ChatGroq #TO INTERACT BW LLM OF OPENAI 
from langchain_core.prompts import ChatPromptTemplate  
from langchain_core.output_parsers import StrOutputParser #IT DECIDES HOW TO SHOW RESPONSE


import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

# envirnment variables call
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

#langsmith tacking 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

#creating chatbot
prompt=ChatPromptTemplate.from_messages(
    [
("system","You are a helpful asistant.please provide response to the user queries"),
("user","Question:{question}")

    ]
)

#streamlit framework     
st.title("langchain demo with groq api")
input_text=st.text_input("Search the topic you want")

#openai llm call
llm=ChatGroq(model="llama3-8b-8192")
output_parser=StrOutputParser()  #display the output in string form

#chain
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
