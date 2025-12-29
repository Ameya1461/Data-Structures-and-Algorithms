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
        
#Q 26- Remove Duplicates in a sorted arrays
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