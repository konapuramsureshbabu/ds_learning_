import numpy as np 
#indexing
arr=np.array([10,20,30,40,50,60])
print(arr[2])
print(arr[-1])

#slicing
print(arr[1:4])
print(arr[:3])
print(arr[1:])

#reshaping
reshaped_array=arr.reshape(2,3)
print(reshaped_array)