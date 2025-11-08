# myarr = [7,2,67,5,87]

# mylist = []
# for index,num in enumerate(myarr):
#     if index % 2 == 0:
#         mylist.append(num)

# print(mylist)


arr = [3,1,2,5,4]    # OP: [4,2,1,3,5]

arr.sort()
centre= arr.pop(0)
rest = arr[:]


arr = [centre]

for index,num in enumerate(rest):
    if index % 2== 0:
        arr.insert(0,num)
    else:
        arr.append(num)
print(arr)