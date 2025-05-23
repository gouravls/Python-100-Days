import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
import ollama
import gradio as gr 
import streamlit as st
import requests

print("How to Start ollama with Mistral in your local systems")
print("We need to perform the following steps:")
print("1. Install ollama in your local system- Go to Google and search for ollama and install it in your local system")
print("2. Install Mistral in your local system- Go to Google and search for mistral and install it in your local system")
print("3. Go to cmd and type 'ollama'")
print("4. Ollama pull mistral")
print("5. Ollama run mistral")  
print("6. Write a prompt")
print("Ctrl + Z")

prompt = "Teach me to run ollama on local system. Give me all the available options related to ollama only, otherwise mention 'question is not related to my domain or out of scope question'."

def teaching_ollama(ollama_question):
    # Corrected the prompt formatting
    prompt = f"""Teach me to run ollama on local system. Give me all the available options related to ollama only, otherwise mention 'question is not related to my domain or out of scope question'.\n\n{ollama_question}"""
    
    # Make the request to Ollama with the provided prompt
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    
    # Extract the content from the response and clean it up
    full_text = response['message']['content'].strip()
    
    return full_text

# Streamlit application setup
st.title("Question and Answer App")

# Dictionary with predefined questions and answers
question = {
    "Run ollama on local system": "1. Download ollama\n2. Go to cmd and type ollama\n3. Ollama pull mistral\n4. Ollama run mistral",
    "Run ollama on local system with Deepseek": "1. Download ollama\n2. Go to cmd and type ollama\n3. Ollama pull deepseek\n4. Ollama run deepseek-r1-latest"
}

# Dropdown for predefined questions
question1 = st.selectbox("Choose a question:", list(question.keys()))

# Display the corresponding answer from the dictionary
st.markdown(f"**Answer:** {question[question1]}")

# Allow the user to ask a custom question
st.subheader("Question you want to ask (not in the list):")
user_prompt = st.text_area("Type your question below:")

# Button to send the user prompt to the Ollama model
if st.button("Ask LLM") and user_prompt.strip():
    with st.spinner("Thinking..."):
        try:
            # Get the response for the user's custom question
            answer = teaching_ollama(user_prompt)
            # Display the LLM response
            st.markdown(f"**LLM Response:** {answer}")
        except Exception as e:
            # Handle errors if something goes wrong
            st.error(f"Error: {e}")
