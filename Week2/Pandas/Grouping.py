# ###Grouping Data by category 

# grouped = df.groupby("Column_name")
# for name , group in grouped :
#     print(name)
#     print(group)

# grouped.mean()
# grouped.sum()

# df.groupby("category_column")["numeric_column"].mean()
# df.groupby("category_column").agg({"numeric_column":["mean","max","min"]})

# pivot = df.pivot_table(
#     values="numeric_column",
#     index="category_column",
#     aggfunc="mean"
# )

# def range_function(x):
#     return x.max()-x.mean()

# df.grouped("category_column")["numeric_column"].agg(range_function)
# df.grouped("category_column")["numeric_column"].mean()
# df.grouped("category_column")["numeric_column"].min()
# df.grouped("category_column")["numeric_column"].max()


# # multi Aggrigation
# df.groupby("category_column").agg(
#     {"numeric_column":["mean","max","min"]}
# )