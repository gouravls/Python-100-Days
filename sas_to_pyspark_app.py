import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
import streamlit as st 
import gradio as gr 
import ollama 
import seaborn as sns 

def sas_to_pyspark(sas_code):
    prompt=f"""Convert this SAS Data Step into equivalent PySpark DataFrame code using Python. Ensure that variable transformations, filters, 
    and column creation are preserved. Assume spark is the active SparkSession.Assuming  a PySpark DataFrame and 'spark' is the active SparkSession
    no extra comments, only code  \n\n{sas_code} """
    response =ollama.chat(model="mistral", messages=[{"role":"user","content":prompt}])
    full_text = response['message']['content'].strip()
    return full_text

dark_theme = gr.themes.Base(
    primary_hue="blue",
    neutral_hue="gray"
).set(
    body_background_fill="#111827",      # Main background (dark)
    body_text_color="#ffffff",           # Main text color (white)
    input_background_fill="#1f2937",     # Input fields
    input_border_color="#4b5563",        # Borders for input fields
    block_background_fill="#1f2937",     # Output panel, etc.
    #block_text_color="#ffffff",          # Text inside blocks
    block_title_text_color="#93c5fd",    # Titles
)

iface = gr.Interface(
    fn=sas_to_pyspark,
    inputs=gr.Textbox(lines=10, placeholder="Enter SAS code here..."),
    outputs="text",
    title="SAS to Pyspark Code Converter",
    description="This tool will convert your SAS code into equivalent pyspark.",
    theme=dark_theme
)

iface.launch(share=True)
#https://your-url-1.gradio.live


