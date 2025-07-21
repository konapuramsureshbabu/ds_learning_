import numpy as np

#reshaping
arr=np.array([1,2,3,4,5,6,7,8,9])
reshaped_array=arr.reshape((3,3))
print(reshaped_array)

#add dimenstional
arr1=np.array([1,2,3])
expanded=arr1[:,np.newaxis]
print(expanded)