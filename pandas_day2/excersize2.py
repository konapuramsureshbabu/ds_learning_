import pandas as pd 
import numpy as np 

df1=pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Alice","Bob","Charlie"],
    "Age":[25,30,34]
})
df2=pd.DataFrame({
    "ID":[1,2,3],
    "Score":[85,90,92]
})

print("First Dataset :\n",df1)
print("Secound Dataset :\n",df2)

merged=pd.merge(df1,df2,how="inner",on="ID")
print("Merged dataset:\n",merged)
merged["Score_Percentage"]=(merged["Score"]/200)*100
print("Transformed dataset:\n",merged)

