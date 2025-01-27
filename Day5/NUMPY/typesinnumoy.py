import numpy as np

type1 = np.array([1, 2, 3, 4, 5, 6])
print("Array : ", type1)
print(type1.dtype)
print("*********"*4)
type2 = np.array([1.5, 2.5, 0.5, 6])
print("Array : ", type2)
print(type2.dtype)
print("*********"*4)
type3 = np.array(['abc', 'bcd', 'cde'])
print("Array : ", type3)
print(type3.dtype)
print("*********"*4)
type4 = np.array(["Nashik", "Solapur"], dtype='U5')  # array with elements of string with length 5
print("Array : ", type4)
print(type4.dtype)
print("*********"*4)
type5 = np.array([123, 432], dtype=float)
print("Array : ", type5)
print(type5.dtype)