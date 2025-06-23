#what is seaborn-->
#Seaborn is a Python data visualization library specializing in creating 
# statistical graphics. It is built on top of Matplotlib and integrates 
# closely with Pandas data structures, making it a powerful tool for exploratory
# data analysis and communicating insights

#common seaborn pots --> heatmap, pairplot

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = np.random.rand(5,5)
# sns.heatmap(data, annot=True,cmap="coolwarm")
# plt.title("HeatMap")
# sns.pairplot(df)

plt.show()