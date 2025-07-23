import pandas as pd
import uuid

# Generate shortened UUIDs (8-character string)
ids = [str(uuid.uuid4()).split('-')[0] for _ in range(4)]

# Create DataFrame
data = {
    "Id": ids,
    "Name": ["Alice", "Bob","Suresh","Raju"],
    "Age": [23, 25,30,66],
    "Gender":["Male","Male","Male","Female"],
    "Adhress":["3/33,HYD,India","3/33,HYD,India","3/33,HYD,India","3/33,HYD,India"]
}

df = pd.DataFrame(data)
print("Head:\n",df.head())
print("Tail:\n",df.tail(3))
print("Info:\n",df.info())
print("Describe:\n",df.describe())
print("Selecting:\n",df[["Age","Name"]])
print("Filtering:\n",df[df["Age"]>23])
print("First Row:\n",df.iloc[0])
print("First Column:\n",df.iloc[:,0])
print("Label:\n",df.loc[0])
print("Selecting Name:\n",df.loc[:,"Name"])



# Save to CSV and Excel
df.to_csv("data.csv", index=False)
df.to_excel("data.xlsx", index=False)
