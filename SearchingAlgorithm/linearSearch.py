# SEARCHING ALGORITHMS #
# Implementation of linear search (also called sequential) --> Recommended for unsorted array
# O(N) , O(1)

def linearSearch(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1

array = [4,2,5,6,9,1]
print(linearSearch(array,5))