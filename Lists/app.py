# # LISTS - holds multiple data types

# # Accessing / Traversing a list

# # shoppingList = ['A', 'B', 'C']
# # print(shoppingList[1])

# # print("a" in shoppingList)

# # INSERTING
# # .append method --> add at the end 
# mylist = [1,2,3,4,5]
# print(mylist)
# mylist.append(6)
# print(mylist)


# # .insert method --> add elemt atr at a particular index
# # ourlist = [1,2,3]
# # print(ourlist)
# # ourlist.insert(0,7)
# # print(ourlist)

# # # Slicing
# # alist = [1,2,3]
# # alist[:3] # --> Just wanted to confirm if we can take an index which is not present as the stop is exclusive (:3 -> prints till index 2)
# # print(alist)

# # # .remove
# # rlist = [1,2,3,4]
# # rlist.remove(2)
# # print(rlist)

# # # Searching an element 
# # numbers = [1,2,3,4,5,6]

# # for num in numbers:
# #     if num == 3:
# #         print("HERE IT IS")

# # LINEAR search
# mylist = [1,2,3,4]
# target = 4
# def linearSearch(list,target):
#     for i,num in enumerate(list):
#         if num == target:
#             return i
#     return -1

# print(linearSearch(mylist,target))

# s = "spam-spam-spam"
# b = s.split('a')
# print(b)

# # modifies the original list directly and does not return a new sorted list.
# marks = [30,40,10,3,5,90,6]
# marks.sort()
# print(marks)



# this_list = [1,2,3]
# new_list = []

# for i in this_list:
#     soln = i * 2 
#     new_list.append(soln)
# print(this_list)
# print(new_list)
# # List comprehension --- condition for item in current_list
# now_list = [i * 3 for i in this_list]  # square bracket
# result = now_list
# print(result)

# language = "python"
# new_char = [char for char in language]
# print(new_char)

# # language = "python"
# # for char in language:
# #     print(char)


# our_list = [10,-2,-4,5,6]
# new_list = [num * num for num in our_list if num < 0 ]
# print(new_list)

# ###################################################################
# # sentence = "This is a Book!!"
# # vowels = "aeiou"

# # ans  = [char for char in sentence if char != vowels ]
# # print(ans)


# sentence = "This is a Book!!"
# vowels = "aeiou"
# answers = []
# for char in sentence:
#     if char not in vowels:
#         answers.append(char)

# print(answers)
    
#     # lower = [char for char in password if char.islower()]
#     #   upper = [char for char in password if char.isupper()]
#     #   numeric = [char for char in password if char.isdigit()]





# class checkPass():

#     def __init__ (self,password):
#         self.password = password

#     steps = 0

#     def lower(self, password):
#         for char in password:
#             if char.islower():
#                 return "OKAY"
#             else:
#                 steps = steps + 1
#         return steps

#     def upper(self, password):
#         for char in password:
#             if char.isupper():
#                 return "OKAY"
#             else:
#                 steps = steps + 1
#         return steps
    
#     def numeric (self, password):
#         for char in password:
#             if char.isdigit():
#                 return "OKAY"
#             else:
#                 steps = steps + 1
#         return steps
    
#     def checkDigit(self,password):
#         if len(password) >= 6 and len(password) <= 20:
#             return "okay"
#         else:
#             steps = steps + 1



# def checkPass(password):
#     lower = [char for char in password if char.islower()]
#     upper = [char for char in password if char.isupper()]
#     numeric = [char for char in password if char.isdigit()]

#     if password >= 6 and password <= 20 and lower and upper and numeric:
#         return "okay"
#     for i,char in enumerate(password):
#         if char[i] == char[i+1] and char[i] == char[i-1]:
#             return "not okay"
#     return "okay"
        

# Average Temperature

# days = int(input("How many day average temperature? "))

# total_temp = []
# for num in range(days):
#     temp = float(input(f"Enter day {num+1}'s temperature: "))
#     total_temp.append(temp)


# avg_temp = sum(total_temp) / len(total_temp)

# print(avg_temp)

# count = 0
# if temp > avg_temp:
#     count= count + 1
# print(f"{count} above avg temp")

# def missing_number(arr, n):
#     # TODO
#     # Calculate the sum of first n natural numbers
#     total = n * (n + 1) // 2
    
# #     # Calculate the sum of numbers in the array
# #     sum_arr = sum(arr)
    
# #     # Find the missing number by subtracting sum_arr from total
# #     missing = total - sum_arr
    
# #     return missing


# def twoSum(nums,target):

#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):

#             if nums[i] + nums[j] == target:
#                 return i,j
            
# arr= [1,2,3,4]
# target = 6

# print(twoSum(arr,target))


# def max_product(arr):
#   # Create a sorted copy of the array
#     product_nums = sorted(arr)  # <-- use sorted() instead of arr.sort()
    
#     # Get product of two largest numbers
#     return product_nums[-1] * product_nums[-2]

# # Example usage:
# myarray = [1, 7, 3, 9, 5]
# print(max_product(myarray))

# def first_second(my_list):
#     # TODO
#     result = sorted(my_list)


#     # reversed(my_list)
#     return result[-1:-2]
# myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# print(first_second(myList))

# list = [1,2,3,4]
# list.insert(2,7)



# mynewlist = [8,6,0]
# list.extend(mynewlist)
# print(list)

# names = ['a', 'b', 'c']
# names.remove('a')
# print(names)

# del list[2]
# print(list)


myarr = [4,3,7,9,2,5]

min = myarr[0]
ans = []
for num in myarr:
    if num < min:
        ans.append(num)
ans.sort()
print(ans[0])
    

