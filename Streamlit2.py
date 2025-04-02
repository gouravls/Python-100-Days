import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as mlt

data1=pd.read_csv("A:\LLM\Sample - Superstore.csv",encoding="latin1")
data1.head()

Category_data2=data1["Category"].unique()
sub_category_data=data1["Sub-Category"].unique()
state_data=data1["State"].unique()
city_data=data1["City"].unique()
segment_data=data1["Segment"].unique()
region_data=data1["Region"].unique()

st.header("E-commerce data")
st.subheader("Focused on data Analaysis")
st.write("e-commarec calculation")
st.markdown("Superstore analysis app")
st.title("Sample Superstore Data Analysis")
st.radio("Select your analysis type",["Category","Sub-Category","State","City","Segment","Region"])
st.selectbox("Select your category:",Category_data2)
st.selectbox("select your sub_category:",sub_category_data)
st.selectbox("select your state:",state_data)

#convert string into date columns
data1["Order Date"]=pd.to_datetime(data1["Order Date"])
data1["Ship Date"]=pd.to_datetime(data1["Ship Date"])

print(data1.columns)
print(data1.dtypes)

#Now extract only year and month part from date columns

data1["Order_year"]=data1["Order Date"].dt.year
data1["Order_month"]=data1["Order Date"].dt.month

#Cocatenate year and month if month contains only one digit then fill will zero
Order_year_month= data1["Order_year"].astype(str)+"-"+data1["Order_month"].astype(str).str.zfill(2)
#for concatenation we are also using the + symbol
#for conver string value astype(str) is used
#to fill the zero in starting of month we are using str.zfill(2)
Order_year_month=Order_year_month.unique()
Order_year_month_sorted=sorted(Order_year_month)
print(Order_year_month_sorted)

st.selectbox("Select your order year month:",Order_year_month_sorted)