## O(N) --> Runs according to the value of N

# def showNumbs(n):
#     for i in range(n):
#         print(i) 
    
# showNumbs(10)

# Droping Constants: 2 times. Hence 2N. But we can drop the 2 since it is a constant
# def showNumbs(n):   
#     for i in range(n): 
#         print(i) 
#     for j in range(n):
#         print(j)
# showNumbs(10)


##  O(n^2) -- result is 4 answers. Total n*n Hence sqaure

# def showNumbs(n):
#     for i in range(n):
#         for j in range(n):
#             print(i,j) 
    
# showNumbs(2)

# Drop non dominant terms: Here 2 time complexity is there for 2 loops hence take time complexity with highest

# def showNumbs(n):
#     # Time Complexity -- O(n^2)
#     for i in range(n):
#         for j in range(n):
#             print(i,j) 
#     # Time Complexity -- O(N)
#     for k in range(n):
#         print(k)
# showNumbs(2)

# def sumNum(num):
#     if num <= 0:
#         return 0
#     return num + sumNum(num - 1)

# result = sumNum(2)
# print(result)

def pairSum(n):
    total = []
    for i in range(n):
        total.append(i + (i + 1))
    return total
    
    
result = pairSum(4)
print(result)