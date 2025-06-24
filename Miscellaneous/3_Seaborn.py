import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


urlprefix = 'https://vincentarelbundock.github.io/Rdatasets/csv/'
dataname = 'MASS/birthwt.csv'
df = pd.read_csv(urlprefix + dataname)


print("Columns in DataFrame:", df.columns.tolist())


if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)


styles = {0: ['o', 'red', 'Non-smoker'], 1: ['^', 'blue', 'Smoker']}


for k in styles:
    grp = df[df.smoke == k]
    m, c = np.polyfit(grp.age, grp.bwt, 1)
    plt.scatter(grp.age, grp.bwt, c=styles[k][1], s=15, linewidth=0,
                marker=styles[k][0], label=styles[k][2])
    plt.plot(grp.age, m * grp.age + c, '-', color=styles[k][1])

plt.xlabel('Age of mother')
plt.ylabel('Birth weight (g)')
plt.legend(prop={'size': 8}, loc='upper right')
plt.title('Birth Weight vs Mother\'s Age by Smoking Status')
plt.grid(True)
plt.tight_layout()
plt.show()
