import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import gradio as gr
import numpy as np
import streamlit as st 
import ollama
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

st.title("What are Type I and Type II Errors")
print("What are Type I and Type II Errors ")
st.markdown("""these comes from hyothesis testing
      We can easily relate to classification problem
      specially binary one
      1:True
      2: False 

      or
      1:-Spam
      2:- Not spam

      or

      1:-Fraud
      2:-legit
""")
print(""" these comes from hyothesis testing
      We can easily relate to classification problem
      specially binary one
      1:True
      2: False 

      or
      1:-Spam
      2:- Not spam

      or

      1:-Fraud
      2:-legit



""")
st.markdown("""just try to understand in layman language

Supposse you are teacher and try to findout someone cheated or not

1:- Nobody has cheated (null hypothesis)
2:-Somebody is cheated (alternative hypothesis)

Now as a teacher you need to make a decision like somebody is cheated or not, but there could be a mistake so that why type1 
and type2 error occurs""")

print("""Just try to understand in layman language

Supposse you are teacher and try to findout someone cheated or not

1:- Nobody has cheated (null hypothesis)
2:-Somebody is cheated (alternative hypothesis)

Now as a teacher you need to make a decision like somebody is cheated or not, but there could be a mistake so that why type1 and type2 error occurs
""")

st.markdown("""
for example teacher comes and say you cheated , but you really did not cheat (It means type1 error)

or teacher says
"Nobody cheated in my class, but some student cheat this (it means type2 error)

""")
print (""" 

for example teacher comes and say you cheated , but you really did not cheat (It means type1 error)

or teacher says
"Nobody cheated in my class, but some student cheat this (it means type2 error)



""")
st.write("In machine learning we can map this to binary classification because in machine learning we have binary classification yes or no, true or false" )
print(" In machine learning we can map this to binary classification because in machine learning we have binary classification yes or no, true or false")

st.markdown("""n True realiity how its works:-

1:True positive:- (model says yes and its really yes)
2:-False positive- (model says yes but in really its not) (type-1 error)
3:-False Negative- (Model says no but in really its yes) (type-2 error)
4:-True negative -(model says no and in really its no)




""")
print("""

In True realiity how its works:-

-1:True positive:- (model says yes and its really yes)




-2:-False positive- (model says yes but in really its not) (type-1 error)



-3:-False Negative- (Model says no but in really its yes) (type-2 error)



-4:-True negative -(model says no and in really its no)





""")

st.subheader("Hypothesis testing")
print ("Hypothesis testing")
st.write("Hypothesis is a method to take decision using data")
print ("Hypothesis is a method to take decision using data")

st.markdown("""Steps in Hypothesis testing

Step1:-H0(null hypothesis):- Nothing is happening
       H1(alternative hypothesis):- Something is happening

Step2:- Collect the data

Step3:- Calculate a test statisc like z-scor or t-score

Step4:-Choose a significance level (α): Usually 0.05 (5%)
This is how willing you are to risk a Type I error (false alarm).

Step 5:- Compare p-value to α:

If p ≤ α → Reject H₀ → evidence for H₁ (something is going on!)

If p > α → Fail to reject H₀ → not enough evidence to say H₁ is true

""")
print(""" Steps in Hypothesis testing

Step1:-H0(null hypothesis):- Nothing is happening
       H1(alternative hypothesis):- Something is happening

Step2:- Collect the data

Step3:- Calculate a test statisc like z-scor or t-score

Step4:-Choose a significance level (α): Usually 0.05 (5%)
This is how willing you are to risk a Type I error (false alarm).

Step 5:- Compare p-value to α:

If p ≤ α → Reject H₀ → evidence for H₁ (something is going on!)

If p > α → Fail to reject H₀ → not enough evidence to say H₁ is true



""")

