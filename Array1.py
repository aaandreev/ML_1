import numpy as np

# from Python list object
a1 = np.array([1,2,3])

# set explicit the data type
a2 = np.array([1,2,3], dtype=float)
a3 = np.array([1,2,3], dtype=bool)


# type coercion
a4 = np.array([1, 2, 3.0])

print(a1)
print(a2)
print(a3)
print(a4)


a2 = np.arange(1,10)
print(a2)
print (a2.reshape(3,3))

a3 = np.arange(0,51)
print(a3[-5: ])

a4 = np.arange(1,10)
print(a4)
a5=a4.reshape(3,3)
print (a5)
print(a5[:,1])
print("------")
print(a5[:,0::2])

