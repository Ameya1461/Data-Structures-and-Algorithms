# import numpy as np

# np_array1 = np.array([1,2,3,4])
# print(np_array1)

import array

# a = [1,2,3,4,5]
# print(a)

# a[2] = 7
# print(a)

array1 = array.array("i", [1,2,3])
# print(array1)
# array1.insert(0,9)
# print(array1)

def linearSearch(array1,target):
    # array1[index] = 0
    for i in range(len(array1)):
        if array1[i] == target:
            return i
        
    return "Not found"
        
result = linearSearch(array1,3)
print(result)