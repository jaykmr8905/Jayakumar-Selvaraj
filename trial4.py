 
##from google import genai
##
##robo = genai.Client(api_key="AQ.Ab8RN6Kgb151bGb2TZNL60262ALtZ2wDtHjy4w7Y8SvgYkJb7Q")
##
##response= robo.models.generate_content(
##    model = "gemini-2.5-flash",
##    contents = "what is Ai give me the 10 of words."
##        )
##print(response.text)





##from google import genai
##
### Create client
##robo = genai.Client(api_key="AQ.Ab8RN6Kgb151bGb2TZNL60262ALtZ2wDtHjy4w7Y8SvgYkJb7Q")
##
### 👇 Take input from user
##user_prompt = input("Enter your question: ")
##
### Generate response using user input
##response = robo.models.generate_content(
##    model="gemini-2.5-flash",
##    contents=user_prompt
##)
##
### Print result
##print("\nResponse:")
##print(response.text)




 
##from google import genai
##
##robo = genai.Client(api_key="AQ.Ab8RN6Kgb151bGb2TZNL60262ALtZ2wDtHjy4w7Y8SvgYkJb7Q")
##
##mychat = robo.chats.create(model="gemini-flash-lite-latest")
##
##coms= ".you are an expert python developer.\
##Answer only questions related to python programming.\
##For any non-python question. reply exactly:\
##Please ask a Python-related question.\
##Do not answer questions outside the python domain."
##
##while True:
##    question = input ("How can i help you:")
##    question = question + coms
##    response = mychat.send_message(question)
##    print(response.text)




##from google import genai
##from google.genai import types
##robo = genai.Client(api_key="AQ.Ab8RN6Kgb151bGb2TZNL60262ALtZ2wDtHjy4w7Y8SvgYkJb7Q")
##
##mychat = robo.chats.create(model="gemini-flash-lite-latest")
##
##config = types.Generatecontenetconfig(
##    System_instruction = ".You are an expert python developer.\
##Answer only questions related to python programming.\
##For any non-python question. reply exactly:\
##Please ask a Python-related question.\
##Do not answer questions outside the python domain."
##    )
##
##
##while True:
##    question = input ("Ask any: ")
##    response = mychat.send_message(question)
##    print(response.text)


##from google import genai
## 
##robo = genai.Client(api_key="AQ.Ab8RN6Kgb151bGb2TZNL60262ALtZ2wDtHjy4w7Y8SvgYkJb7Q")
## 
##mychat = robo.chats.create(model="gemini-flash-lite-latest")
## 
##coms = "You are an expert of Python developer.\for any non-python question. reply exactly:\
##Please ask a Python-related question.\
##Do not answer questions outside the python domin."
## 
## 
##while True:
##        question = input ("How can i help you: ")
##        question = question + coms
##        response = mychat.send_message(question)
##        print(response.text)


##from google import genai
## 
##robo = genai.Client(api_key="AQ.Ab8RN6Kgb151bGb2TZNL60262ALtZ2wDtHjy4w7Y8SvgYkJb7Q")
## 
##mychat = robo.chats.create(model="gemini-flash-lite-latest")
## 
##coms = "You are an expert of GOOGLE."
## 
## 
##while True:
##        question = input ("How can i help you: ")
##        question = question + coms
##        response = mychat.send_message(question)
##        print(response.text)

##from google import genai
##
##robo = genai.Client(api_key="AQ.Ab8RN6KHFRTiCL6LRWEsYmbXlOWzdsk2hGFMZ1A-uBm-OTgEdA")
##mydata = robo.files.upload(file="C:\\Users\jselvara\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python\Python 3.14\\Wolf.jpg")
##mychat = robo.chats.create(model="gemini-flash-lite-latest")
##while True:
##        question = input("ask any:")
##        response = mychat.send_message([question,mydata])
##        print(response.text)

##import streamlit
##streamlit.title("My AI")

##import streamlit as st
##from google import genai
##robo = genai.Client(api_key="AQ.Ab8RN6KHFRTiCL6LRWEsYmbXlOWzdsk2hGFMZ1A-uBm-OTgEdA")
##mychat = robo.chats.create(model="gemini-flash-lite-latest")
##st.title("J - Ai")
##
##question = st.text_input("Aks any")
##if st.button("Send"):
##  response = mychat.send_message(question)
##  st.write(response.text)

##import streamlit as st
##from google import genai
##
##st.markdown(
##    """
##    <h1 style='text-align: center;'> JAI AI Assistant</h1>
##    <p style='text-align: center; font-size:18px;'>
##    Ask any Python programming question.
##    </p>
##    """,
##    unsafe_allow_html=True,
##)
##
##robo = genai.Client(api_key="AQ.Ab8RN6KHFRTiCL6LRWEsYmbXlOWzdsk2hGFMZ1A-uBm-OTgEdA")
##mychat = robo.chats.create(model="gemini-flash-lite-latest")
##
### Placeholder for the response
##response_placeholder = st.empty()
##
##question = st.text_input("", placeholder="Enter your Python question here...")
##
##col1, col2, col3 = st.columns([1, 1, 2])
##
##with col2:
##    send = st.button("Send")
##
##if send:
##    response = mychat.send_message(question)
##    response_placeholder.write(response.text)
##

import streamlit as st
from google import genai
import os

st.set_page_config(page_title="JAI AI Assistant", layout="centered")

# Colourful background + styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    }
    h1 {
        color: #1E3A8A;
        text-align: center;
        font-weight: 800;
    }
    p {
        text-align: center;
        font-size: 18px;
        color: #FFFFFF;
    }
    .stTextInput input {
        border-radius: 10px;
        border: 2px solid #1E3A8A;
    }
    .stButton button {
        background-color: #1E3A8A;
        color: white;
        border-radius: 10px;
        font-weight: 600;
    }
    .stButton button:hover {
        background-color: #2563EB;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h1><span style='color:#1E3A8A;'>j-AI</span> Assistant</h1>
    <p>Ask any question.</p>
    """,
    unsafe_allow_html=True,
)

robo = genai.Client(api_key="AQ.Ab8RN6KHFRTiCL6LRWEsYmbXlOWzdsk2hGFMZ1A-uBm-OTgEdA")
mychat = robo.chats.create(model="gemini-flash-lite-latest")

# Placeholder for the response
response_placeholder = st.empty()

question = st.text_input("", placeholder="Enter your question here...")

col1, col2, col3 = st.columns([1, 1, 2])

with col3:
    send = st.button("GO")

if send:
    response = mychat.send_message(question)
    response_placeholder.write(response.text)
