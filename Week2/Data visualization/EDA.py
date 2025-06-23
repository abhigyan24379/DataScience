#Exploratory Data Analysis 
# --> it is a cruccial initial stepo in data analysis where  we 
# examine  and summarize the data and understand its main characteristic 
# it involves using visualization and statistical technique and uncover patterns,
# identify anomalies and formulate hypotheses. EDA helps us to understand the  data structre ,
# assess data qualties and choose appropriate analysis methods  

# Step in EDA 
# --> data cleaning 
# --> data transformation 
# --> aggregation and filtering 

# Identify Patter,Trends, Correlation
# - visual tools for insights 
#   -> line plot for trend  over time 
#   -> bar charts for categorical comparisons
#   -> scatter plots for relationships
#   -> Heatmaps for correlation analysis


# Key patterns to look for 
#  -> realtionship between variables (correlation)
#  -> distribution of variable (histograms, boxplots)
#  -> outliners or anomalies 


# Summary statistics, visual insights and hypothesis generation
#  -> Summary Statics 
#  -> Hypothesus Generation 

# DataSet link --
#  -->  "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#loading the Data 
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"
df = pd.read_csv(url)

#Inspect Data 
print (df.info() )
print (df.describe())

# Handle missing Values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

#remove duplicates
df= df.drop_duplicates()

#filter data : passengers in first class
first_class = df[df["Pclass"]==1]
print ("first class Passengers :\n", first_class.head())

#bar chart survival rate by class 
survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color="skyblue")
plt.title("Survival rate by class")
plt.ylabel("survival rate ")
plt.show()

#Histogram :  Age distribution 
sns.histplot(df["Age"],kde=True,bins=20,color="purple")
plt.title("Age distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#scatter Plot Age vs Fare
plt.scatter(df["Age"],df["Fare"], alpha=0.5, color="green")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()