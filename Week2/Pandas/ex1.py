#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv
import pandas as pd 


# Load Dtaset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# #explore structure 
# print("first 5 row ",df.head())
# print("Last 5 row ",df.tail())
# print(df.info())
# print(df.describe())

select_columns = df[["species","sepal_length"]]
print("Selected columns ", select_columns)

filtered_rows = df[(df["sepal_length"]> 5.0) & (df["species"] == "setosa")]
print("filtered rows", filtered_rows)

