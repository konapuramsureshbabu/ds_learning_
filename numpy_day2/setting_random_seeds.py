import numpy as np 

#for seeding random nums (const random number on every time ),give any number in brackets 
np.random.seed(22)

random_array=np.random.rand(3,3)
print("Random Array=>",random_array)

#generate the integer instead of floats
random_integers=np.random.randint(0,10,size=(2,3))

print("Random Integer",random_integers)