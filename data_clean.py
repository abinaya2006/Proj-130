from os import remove
import pandas as pd


df=pd.read_csv("total_stars.csv")
print(df.shape)

del df["Luminosity"]
del df["star_name"]
del df["distance"]
del df["mass"]
del df["radius"]


df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.drop(['Unnamed: 6'],axis=1,inplace=True)
df.to_csv("final.csv",index=False)