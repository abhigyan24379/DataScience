import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

xls = 'http://www.biostatisticien.eu/springeR/nutrition_elderly.xls'
nutri = pd.read_excel(xls)
# print (nutri)

nutri.info()
DICT = {1:'Male', 2:'Female'} # dictionary specifies replacement
nutri['gender'] = nutri['gender'].replace(DICT).astype('category')

nutri['height'] = nutri['height'].astype(float)
nutri.to_csv('nutri.csv',index=False)
nutri = pd.read_csv('nutri.csv')
nutri['fat'].describe()
nutri['fat'].value_counts()
pd.crosstab(nutri.gender, nutri.situation)
pd.crosstab(nutri.gender, nutri.situation, margins=True)
print( nutri['height'].max()- nutri['height'].min())

print(round(nutri['height'].var(), 2) )# round to two decimal places
 
width = 0.35
x = [0,0.8,1.6] 
situation_count = nutri['situation'].value_counts()
plt.bar(x,situation_count,width , edgecolor = "black")
plt.xticks(x, situation_count.index)
plt.show ()
 
plt.boxplot(nutri['age'],widths =width,vert=False)
plt.xlabel("Age")
plt.show()
