import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title("Sample Superstore Data Analysis")
st.header("e-commerce data")
st.subheader("Focused on profit and sales")
st.write("e-commerce data analysis")
st.markdown("Superstore analysis app")

if st.button("click me"):
    st.write("I am clicked")

info1=st.text_input("Enter your info1") 
info2=st.text_area("Enter your info2")  
st.write("info1:", info1)
st.write("info2:", info2) 

age=st.slider("Enter your age year",1,80,2)
st.write("age",age)

data1=pd.read_csv("A:\LLM\Sample - Superstore.csv",encoding="latin1")
data1.head()
data2=data1.describe()
st.table(data1.head(10)) #static table
st.dataframe(data2) #dynamic table
category1=data1["Category"].unique()
st.selectbox("Select your category:",category1)
st.radio("Select your sub_category:",data1["Sub-Category"].unique())
st.button("Select your state",data1["State"].unique())
data2 = data1.groupby("Category")["Profit"].sum()
st.line_chart(data2)
fig, ax = plt.subplots()
ax.bar(data1["Category"], data1["Profit"], color='blue')
#profit_plot=plt.bar(data1["Category"],data1["Profit"],color='blue')
plt.title("Profit Plot")
plt.xlabel("Index") 

st.pyplot(fig)