import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

mydata = pd.read_csv('CardioGoodFitness.csv')
print (mydata.head())

print(mydata.describe(include='all'))


