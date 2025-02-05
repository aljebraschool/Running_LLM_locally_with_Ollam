#import needed libraries
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

### using Langsmith for tracing your model
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
langchain_project = os.getenv("LANGCHAIN_PROJECT")
langchain_tracing = os.getenv("LANGCHAIN_TRACING_V2", 'true')


#design prompt template
template_string = """
As a chatbot assistance please response to the question asked by user:
question : {question}

"""

prompt_template = ChatPromptTemplate.from_template(template_string)

# Streamlit framework
st.title("LANGCHAIN DEMO WITH LLAMA2")
input_text = st.text_input("Type you question in this box")

#build the model
llm = Ollama(model = 'llama2')

output_parser = StrOutputParser()

chain = prompt_template | llm | output_parser

#show your output
if input_text:
    st.write(chain.invoke({"question": input_text}))
