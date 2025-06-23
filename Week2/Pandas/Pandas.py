#Pandas is an open-source software library for the Python programming language,
# primarily used for data manipulation and analysis. It provides powerful 
# and flexible data structures, most notably the DataFrame and Series, which 
# are designed to work efficiently with tabular and time-series data. 

#pandas Data Structure 
# --> Series -- Series: A one-dimensional labeled array capable of holding 
# any data type.
# --> DataFrame -- DataFrame: A two-dimensional, size-mutable, tabular data 
# structure with labeled axes (rows and columns), similar to a spreadsheet or
# SQL table.

import pandas as pd 

s = pd.Series([10,20,30], index=["a","b","c"])
# print(s)

# data = {"Name ":["Alice ", "Bob"], "Age ":[25, 30]}
# df= pd.DataFrame(data)
# print (df)


#what is csv file --> A CSV (Comma Separated Values) file is a plain text file
# format used to store tabular data, where each row represents a record and 
# the values within each row are separated by commas. Essentially, it's a 
# simple way to represent data in a spreadsheet-like structure using text. 

# methods by which we can read the file directly and use it 

# df = pd.read_csv("data.csv")
# df.to_csv("data.csv") --> helps in saving the data in the csv format
# df = pd.read_excel("data.xlsx")
# df = pd.to_excel("data.xlsx") --> saves as xl file 


# viewing data 
# print(df.head())  #--> shows first 5 data 
# print(df.tail())  #--> shows last 5 data 
# print (df.info()) #--> provide info 
# print (df.describle())  

# print (df[["Name","Age"]])  #filte the dataset by name and age 
# print (df[df["Age"]>25 ])   #filter the data set where the age is greater then 25

# print (df.iloc[0])    # gives first row by position
# print (df.iloc[:,0])  # first column by position 

# print (df.loc[0])    # gives first row by index label 
# print (df.loc[: , "Name"])    # gives first column  by Name


