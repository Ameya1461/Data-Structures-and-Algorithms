# Q1
# 2 Sum


# class Solution: O(N**2)
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # for i in range(len(nums)):
#         #     for j in range(i+1, len(nums)):

#         #         if nums[i] + nums[j] == target:
#         #             return i, j
        ############################################################
        # OPTIMAL SOLUTION - O(N)
#         hashmap = {}  # num : index
#         for i, num in enumerate(nums):
#             difference = target - num
#             if difference in hashmap:
#                 return hashmap[difference], i
#             hashmap[num] = i
#         return
        
# Q3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    

# Q125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        charset = []
        for char in s.lower():
            if char.isalnum():
                charset.append(char)


        left = 0
        right = len(charset) - 1
        while left < right:
            if charset[left] != charset[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
        
# Q26- Remove Duplicates in a sorted arrays
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         digitSet = []
#         for i in range(0, len(nums) -1 ):
#             for j in range(i + 1, len(nums) - 1):
#                 if nums[i] != nums[j]:
#                     continue
#                 nums.pop(j)
#         # return len(nums)
#         # return list((nums))
#         print(list(set(nums)))        


# Q66- Plus One
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         for i in range(len(digits) - 1, -1, -1):
#             if digits[i] < 9:
#                 digits[i] += 1
#                 return digits
#             digits[i] = 0
#         return [1] + digits
        

# Q41 First Missing Positive
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         dictTrack = {}
#         smallestPositiveNum = 1
#         for i in range(len(nums)):
#             if nums[i] not in dictTrack:
#                 dictTrack[nums[i]] = i
#         while smallestPositiveNum in dictTrack:
#             smallestPositiveNum += 1
#         return smallestPositiveNum


# Q136 - Single Number
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         result = 0  # To store the XOR value
#         for num in nums:
#             result = num ^ result
#         return result

        # brute force - O(N) both below soln
        # dictSet = {}
        # for i in range(len(nums)):
        #     if nums[i] not in dictSet:
        #         dictSet[nums[i]] = 1
        #     else:
        #         dictSet[nums[i]] = 2
        # for key in dictSet:
        #     if dictSet[key] == 1:
        #         return key


# Q34
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:

        # i = 0
        # result = []
        # while i < len(nums):
        #     if nums[i] == target:
        #         result.append(i)
        #     i += 1
        # if not result:
        #     return [-1, -1]
        # return [result[0], result[-1]]

        # binary search
        # def leftBS():
        #     l = 0
        #     r = len(nums) - 1
        #     i = -1
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if nums[mid] >= target:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
                
        #         if nums[mid] == target:
        #             i = mid
            
        #     return i

        # def rightBS():
        #     l = 0
        #     r = len(nums) - 1
        #     i = -1
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if nums[mid] <= target:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
                
        #         if nums[mid] == target:
        #             i = mid
            
        #     return i
        # return (leftBS(), rightBS())

# Q27 - REMOVE ELEMENT
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         # 2 pointer approach
#         i = 0
#         for j in range(len(nums)):
#             if nums[j] != val:
#                 nums[i] = nums[j]
#                 i += 1
#         return i

## Q80 
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         j = 1
#         count = 1
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 count += 1
#             else:
#                 count = 1
#             if count <= 2:
#                 nums[j] = nums[i]
#                 j += 1
#         return j
## KEEPING j so that we can replace with nums[i] if count goes beyond 2
## 1 1 1 2
#       j i  --> replace it 


# Q53 
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         current_sum = nums[0]
#         max_sum = nums[0]

#         for i in range(1, len(nums)):
#             current_sum = max(nums[i], current_sum + nums[i])
#             max_sum = max(max_sum, current_sum)

#         return max_sum

        # current_sum = 0
        # maxresult = nums[0]
        # for i in range(len(nums)): # 1
        #     for j in range(i, len(nums)):
        #         current_sum += nums[j]  # 
        #         if current_sum > maxresult:  # 
        #             maxresult = current_sum  # 2
        #     current_sum = 0
        # return maxresult
            
