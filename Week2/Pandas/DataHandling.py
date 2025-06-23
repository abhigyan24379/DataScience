
# ### Handling missing values 
# ##--> why handling missing values: Missing values are a common issue in machine 
# # learning. This occurs when a particular variable lacks data points, resulting 
# # in incomplete information and potentially harming the accuracy and dependability 
# # of your models. It is essential to address missing values efficiently to 
# # ensure strong and impartial results in your machine-learning projects.
# ## methods to handle missing values --> drop missing values , fill missing values , interpolation 


# df = df.dropna()
# df = df.dropna(axis =1 )

# df["column_name"] = df["column_name"].filena(0)

# df.fillna(method="ffill")
# df.fillna(method="bfill")

# df["column_name"] = df["column_name"].interpolate()


# ### Data transformations
# ##--> renaming columns, changing datatypes , creating or modifying columns 


# df = df.rename(columns ={"old_name":"new_name"})
# df["column_name"] = df["column_name"].astype("float")
# df["column_name"] = pd.to_datatime(df["column_name"])

# df["new_column"] = df["existing_column"] * 2


# ### combning and merginf DataFrame
# ## --> concatenation , merging, joining 

# combined = pd.concat([df1,df2], axis =0)
# combined = pd.concat([df1,df2], axis =1)

# merge = pd.merge(df1,df2, on="common_column")
# merge = pd.merge(df1,df2,how="left", on="common_column")
# merge = pd.merge(df1,df2,how="inner", on="common_column")

# joined = df1.join(df2 , how ="inner")

