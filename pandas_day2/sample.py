import pandas as pd 
import numpy as np 

#create a sample data set

data={
    "Name":["Alice","Bob",np.nan,"David"],
    "Age":[24,np.nan,30,35],
    "Score":[85,90,np.nan,88]
}
#converting a dictionary into Data frame
df=pd.DataFrame(data)

print("Original DF:\n",df)

#fill the missing values with mean 
df["Age"]=df["Age"].fillna(df["Age"].mean())
#fill the missing value with interploate method
df["Score"]=df["Score"].interpolate()

print("modified after fill:\n",df)

df=df.rename(columns={"Name":"Student_name","Score":"Exam_score"})

print("after rename the columns:\n",df)
