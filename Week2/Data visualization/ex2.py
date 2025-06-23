# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

#load Dataset 
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
del df['species']
#calculate corelation matrix
corelation_matrix = df.corr()

#plot heatmap
sns.heatmap(corelation_matrix,annot= True ,cmap="coolwarm")
plt.show()