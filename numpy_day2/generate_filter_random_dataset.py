import numpy as np 

#generate random dataset
dataset=np.random.randint(1,51,size=(5,5))
print("Original: \n",dataset)

#filter values >25 and replace with 0
dataset[dataset>25]=0
print("Modified:\n",dataset)

#calculate the summary stats

print("sum:\n",np.sum(dataset))
print("mean:\n",np.mean(dataset))
print("Standared Deviation:\n",np.std(dataset))