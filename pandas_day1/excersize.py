#https://github.com/mwaskom/seaborn-data/blob/master/iris.csv

import pandas as pd

#Load data set
df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/iris.csv")
#Explore structure
print("First 5 rows:\n",df.head())
print("Last 5 rows:\n",df.tail())
print("Info:\n",df.info())
print("Describe:\n",df.describe())

slected_columns=df[["species","sepal_length"]]

print("My selected Columns:\n",slected_columns)

filter_rows=df[(df["sepal_length"]>5.0) & (df["species"]=="setosa")]
print("filter_rows:\n",filter_rows)