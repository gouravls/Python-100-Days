import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st 
import gradio as gr
import ollama
import re

def convert_sas_to_python(sas_code):
   prompt=f"""Convert the following SAS code to Python using Pandas. Ensure equivalent logic, variable names, 
   and transformations are preserved. Replace SAS procedures (proc, data, set, etc.) with Pandas equivalents. 
   Handle conditional logic, groupings, joins, imports, exports, and formatting as per Pandas syntax.
    Notes:
    - Translate SAS `DATA`, `SET`, and `PROC` steps into equivalent pandas operations.
    - Use `.groupby()`, `.agg()`, `.merge()`, and other pandas idioms where appropriate.
    - Replace SAS formats and functions (like `IF`, `WHERE`, `BY`) with pandas equivalents.
    
    :\n\n{sas_code}"""
   response =ollama.chat(model="mistral", messages=[{"role":"user","content":prompt}])
   #return response['message']['content']
   #bigquery_sql = response['message']['content'].strip()
   #why we used below code here
   #aisa ouput aayega if we run the ollama chat code, Now here we need message part and in message part we need content part only
   '''response = {
    'message': {
        'role': 'assistant',
        'content': 'SELECT * FROM employees;'
    },
    'created_at': '2024-04-05T12:34:00Z',
    'model': 'mistral',
    'done': True
}
'''

   full_text = response['message']['content'].strip()
   # Extract SQL inside triple backticks
   match = re.search(r"```(?:sql)?\s*(.*?)```", full_text, re.DOTALL | re.IGNORECASE)
    
   if match:
        bigquery_sql = match.group(1).strip()
   else:
        # Fallback to original response if no code block found
        bigquery_sql = full_text
   return bigquery_sql

import gradio as gr

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
    fn=convert_sas_to_python,
    inputs=gr.Textbox(lines=10, placeholder="Enter SAS code here..."),
    outputs="text",
    title="SAS to Pandas(python) Code Converter",
    description="This tool will convert your SAS code into equivalent Pandas(python) ."
)

iface.launch(share=True)


'''dark_theme = gr.themes.Base(
    primary_hue="blue",
    neutral_hue="gray"
).set(
    body_background_fill="#111827",  # Dark background
    body_text_color="#ffffff",       # White text
    input_background_fill="#1F2937", # Input box
    input_text_color="#ffffff",
    block_background_fill="#1F2937", # Panel backgrounds
    block_border_color="#374151",    # Subtle borders
)

# Set up Gradio interface
iface = gr.Interface(
    fn=convert_sas_to_python,                # Function to call
    inputs=gr.Textbox(lines=10, placeholder="Enter SAS code here..."),  # Input box for SAS code
    outputs="text",                            # Output will be BigQuery SQL
    title="SAS to BigQuery Code Converter",     # Title for the app
    description="This tool will convert your SAS code into equivalent BigQuery SQL. Just paste your SAS code and get the result.",  # Description
    theme="default-dark"
)



# Launch the Gradio interface
iface.launch(share=True)
'''