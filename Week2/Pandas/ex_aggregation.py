import pandas as pd

data ={
    "class":["A","B","A","B","C","C"],
    "Score":[85,90,98,72,95,90],
    "Age":[15,16,15,17,16,15]
}

df = pd.DataFrame(data )

print("Original database \n",df)

grouped = df.groupby("class").mean()
# print(grouped)

stats =df.groupby("class").agg(
    {"Score":["mean","max","min"], "Age":["mean","max","min"]}
)
print(stats)