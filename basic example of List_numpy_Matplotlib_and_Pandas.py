import numpy as np 
data=[220,330,440,550,660,770,770]
print(data)
#removing duplicate from the list
data1=set(data)
print(data1)
#find the max number from the list
data2=max(data)
print(data2)
#find the min number from the list
data3=min(data)
print(data3)
#count the total number of elements in the list
data4=len(data)
print(data4)
#do you know list can store all types elements either its string, integer or number
new_data=[220,'cpbm','benefit',22.34]
print(new_data)

#if you want to access any elemnets from sql or SAS we are using
#select col1 from table1

#Here in list you can use indexing

data5=new_data[1]
print(data5)

#what if you need mutiple values then we can use slicing

data6=new_data[1:3]
print(data6)

#for example if you want to reverse a list
data7=new_data[::-1]
print(data7)

#if you need the last element
data8=new_data[-1:]
print(data8)

#if you need second last element
#make sure if you fetching last or second last element from the list then you can use -1 or -2 like that
data9=new_data[-2]
print(data9)

#if you need  last element

data10=new_data[-1]
print(data10)

#if you need last and second last both then you can use indixing
data11=new_data[-2:]
print(data11)

#main advanatage of python is we can add new elements in the list, we can delete few elements from the list
#for example in sql if we want to anything new
#insert into 

data12=data
data12[4]=99999 #at fourth position new element is added
print(data12)

#for add new elements we can use the append function as well.
data12.append(100001)
print(data12)

#but please make sure if you are using assignment (means assigning new value then it will not assign with list function)
data13=data12.append(100001)
print(data13)
#this will print output none

#how to remove an element from the list
#in sql we are using delete from 

data12[1]=''
print(data12)

#we can use del function

del data12[5]
print(data12)

#how to count an element
#select count(*) from table1

data13=len(data12)
print(data13)

#do loop in sas

for i in data:
    print(i)


#sort the data from the list
#select * from table order by col1#
new_data1=[33,44,55,699,222,444,551,432]
new_data1.sort(reverse=True)
print(new_data1)

#how to perform union in list
#union means removing duplicate when combining
list1=[10,20,30,40,50,60]
list2=[50,60,70,80,90]
final_list =list(set(list1+list2)) 
print(final_list)

#for example if we want to apply union all on this
#then we donot need to remove the duplicate

final_list1 = list1+list2
print(final_list1)

#how to apply filter on this
#select * from where emp=1

employee =[{'name':"john", 'salary': 60000},
        {'name':'Michael', 'salary':70000}]

#list comprehension
high_sal=[i for i in employee if i['salary']>61000 ]  
print(high_sal)    

#list comprehension is a shortest form of for loop
#for example if we need to write the same logic we can write in this way as well.abs

high_sal1=[]
for i in employee:
    if i['salary']> 60000:
        high_sal1.append(i)

print(high_sal1)


/****************************************************************************************************************************************\
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
data={'Month':["Jan", "Feb","Mar", "Apr", "May", "June", "July" ,"Aug", "Sep","Oct","Nov","Dec"],
      "Revenue" :[10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000],
      "profit" :[10,20,30,12,13,12,12,13,14,15,12,17]
 }

print(data)

#Here we are taking any key from the dataframe
#for example we have taken profit
#Please make sure to use plt.show() otherwise no results
df= pd.DataFrame(data)
plt.plot(df['profit']) 
plt.show()

plt.plot(df["profit"],color='green')
plt.show()

#here linestyle means what kind of lines you want to present
#marker is used to points( as name suggest mark all the points)
plt.plot(df["profit"],color='green',label = "profit", linestyle ='--' , marker ='s')
plt.title("Profit details of this diff year")
plt.xlabel('month', fontsize=12)
plt.ylabel("Profit in percentage")
plt.legend()
plt.grid(True) #in background if you wants diff lines then we are using grid
plt.show()


/********************************************************************************************************************************\
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#Customer segmentation & behavoor analaysis
#Analyzing customer spending appterens

data= {'Product_Name':['Bookcases','Chairs','Labels','Tables','Storage','Furnishings','Art','Phones','Binders'],
       'Sales' :[261.96,731.94,14.62,957.5775,22.368,48.86,7.28,907.152,18.504],
       'Quantity' :[2,3,2,5,2,7,4,6,3],
       'discount' : [0,0,0,0.45,0.2,0,0,0.2,0.2]
}
	

print(data)

df= pd.DataFrame(data)

#creating plot grph here
#creating line graph here
plt.plot(df["Sales"], color='green',linestyle='--',marker='s',label="Sales")
plt.plot(df["Quantity"], color='black',linestyle=':',marker='s', label="Quantity")
#plt.plot(df["discount"], color='orange',linestyle=':',marker='s',label="discount")
plt.title("Sales Vs Quantity")
plt.legend()
plt.grid()
plt.show()

#creating histogram here
#Now just imagine if we want to print in histogram
plt.hist(df["discount"], color="red", label="discount")
plt.title("discount in details")
plt.xlabel("discount_in_points", fontsize=12)
plt.ylabel("data_available", fontsize=10)
plt.grid()
plt.legend()
plt.show()

#creating bar grph here
#for bar graph we need two variable one category_variable and anothe value
plt.bar(df["Product_Name"],df["Sales"], color='blue', label="sales")
plt.title("Product vs Sales")
plt.grid()
plt.legend()
plt.xlabel("product_detail")
plt.ylabel("sales_detail")
plt.show()



#creating line graph, passing two variables

plt.plot(df["Sales"], df["Quantity"], color="green", marker='o', label="sales")
plt.title("Sales vs Quantity")
plt.xlabel("points")
plt.ylabel("y_value")
plt.grid()
plt.legend()
plt.show()


#generate scatter plot

x=np.random.rand(50)
y=np.random.rand(50)

plt.scatter(x,y)
plt.show()

/**************************************************************************************\

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import csv as cs

#data1=pd.read_csv("C:\Users\gsikka\'OneDrive - '\Documents\sample.csv", encoding="latin1")
#data1=pd.read_csv("C:\Users\gsikka\'OneDrive - '\Documents\sample.csv", nrows=10)
#data1=pd.read_csv("C:\Users\gsikka\'OneDrive - '\Documents\sample.csv", sep=",")
#data1=pd.read_csv("C:\Users\gsikka\'OneDrive - '\Documents\sample.csv", header=1)
#data1=("C://Users//gsikka//OneDrive - //Documents//sample.csv")
#print(data1)
#with open("C:\\Users\\gsikka\\OneDrive - \\Documents\\sample.csv", "rb") as f:
     #  print(f.read(100))
# #with open("C:\\Users\\gsikka\\OneDrive - \\Documents\\sample.csv", "r",) as f:
#        reader = cs.reader(f)
#        for i, row in enumerate(reader):
#            print(row)
#            if i > 5:
#                break

data1=pd.read_csv("C:\\Users\\gsikka\\OneDrive - \\Documents\\sample.csv", encoding="cp1252") 
df=pd.DataFrame(data1)
#print(data1.head()) 
#slicing for reading the data
data2=data1[1:10]
print(data2)

#if you want only columns
print(data2.columns)

#last 5 records
print(data1.tail())

#it will tell all the null columns as True otherwise false
print(data2.isnull())

#Sum of null values , according to columns wise
print(data2.isnull().sum())

#isnull and isna both are kind of same thing
print(data2.isna())

#describe will work similar to proc means it will show count, mean, std, min, 25%,50% etc
data3=data1.describe()
print(data3.head(20))

plt.plot(data1['Quantity'], color='green', label="quant")
plt.grid()
plt.title("Quantity describe")
plt.xlabel("quantity_in_x", fontsize=12)
plt.ylabel("quantity_in_y", fontsize=12)
plt.legend()
plt.show()
plt.plot(data1['Profit'], color='blue')
plt.grid()
plt.title("profit display")
plt.show()

#Do you know we can take two varaiables in plt.plot

plt.plot(df["Sales"], df["Quantity"], color="red", marker='o', label="sales")
plt.title("Sales vs Quantity")
plt.xlabel("points", fontsize=12)
plt.ylabel("y_value", fontsize=12)
plt.grid()
plt.legend()
plt.show()

plt.plot(df["Sales"], df["Profit"], color="black",label="Salesss", marker="o")
plt.xlabel("Sales_value")
plt.ylabel("Profit_values")
plt.legend()
plt.grid()
plt.show()


plt.bar(df["Ship Mode"], df["Sales"], color='green', label="Ship Mode")
plt.title("Ship_mode vs Sales")
plt.grid()
plt.legend()
plt.xlabel("Ship_mode")
plt.ylabel("Sales")
plt.show()

/**********************************************************************************************\

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

data1=pd.read_csv("C:\\Users\\gsikka\\OneDrive - \\Documents\\sample.csv", encoding="cp1252") 
print(data1.head())

print(data1.info())

data2=data1.describe()
data3=data2.T
print(data3)

data4=data3.transpose()
print(data4)

#to check the total number of rows and columns
data1.shape
print(data1.shape)

#to check columns
data1.columns
print(data1.columns)

#slicing on data
data1[5:15]
print(data1[5:15])

data10=data1["profit"]
print(data10)





