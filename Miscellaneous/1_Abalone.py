import pandas as pd 
abalone = pd.read_csv('abalone.data',header=None)
# print (abalone)

urlprefix = 'https://vincentarelbundock.github.io/Rdatasets/csv/'
dataname = 'datasets/iris.csv'
iris = pd.read_csv(urlprefix + dataname)

# print (iris)

# iris = iris.drop ('unnamed: 0',1)
# print (iris)

abalone.columns= ['Sex', 'Length', 'Diameter','Height','Whole weight','Shucked weight','Viscera weight','Shell weight', 'Rings']
# print(abalone)

# print(abalone['Sex'].describe())
# print(pd.crosstab(abalone.Sex, abalone.Length ))
# print(abalone['Height'].quantile(q=[0.25,0.5,0.75]))

#Standard deviation 
print(abalone['Height'].max() - abalone['Height'].min())

print (round(abalone["Shell weight"].var(), 2)) # rounds to two decimal places 
