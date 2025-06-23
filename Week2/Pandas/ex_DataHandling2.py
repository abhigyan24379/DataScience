import pandas as pd 
import numpy as np

df1 = pd.DataFrame({
    "id":[1,2,3],
    "Name":["Alice", "Bob","Charlie"],
    "Age" :[25,30,35]
})

df2 = pd.DataFrame({
    "id":[1,2,3],
    "Score":[85,90,88]
})

print("DataSet1 :",df1)
print("Dataset2 :", df2)

merged = pd.merge(df1,df2,how="inner", on="id")
print("Merged Dataset \n", merged)