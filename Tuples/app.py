# Implementation of Tuples --> comma sperated values
# only supports .index() and .count() methods

t = 'a', 'b', 'c'
print(t)


t1 = ('a', 'b', 'c', 'd')
for i in range(len(t1)):
    print(t1[i])

# print(t1.index('a'))
print('a' in t1)


t1 = ('a', 'b', 'c', 'd')
def searchElement(tup, element):
    for char in t1:
        if char == element:
            return f"Found  {element}"
    return "Not Found!!!"

print(searchElement(t1,'r'))

input_tuple = (1, 2, 3, 4)
def sum_product(input_tuple):
    # TODO
    # sum_result = sum(input_tuple)
    # return sum_result
    product_result = 1
    for i in range(len(input_tuple)):
        product_sum =  input_tuple[i] * product_result 
        product_result = product_sum
    # return product_result
    
    sum_result = sum(input_tuple)
    return sum_result,product_result

print(sum_product(input_tuple))

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

for num in input_tuple:
    print(num)