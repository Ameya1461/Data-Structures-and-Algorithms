# Q344 - Reverse String
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         l = 0
#         r = len(s) - 1

#         while l <= r:
#             s[l], s[r] = s[r], s[l]
#             l += 1
#             r -= 1
#         return s


# Q125 - Valid Palindrome
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         charset = []
#         for char in s.lower():
#             if char.isalnum():
#                 charset.append(char)
#         # return charset

#         left = 0
#         right = len(charset) - 1
#         while left < right:
#             if charset[left] != charset[right]:
#                 return False
#             else:
#                 left += 1
#                 right -= 1
#         return True
        
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

# Q567
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        
        # Initialing storing value of each char as 0
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        # s1 = [97 98]  s2 = [103 107]  ASCII values
        for i in range(n1):
            count_s1[ord(s1[i]) - 97] += 1
            count_s2[ord(s2[i]) - 97] += 1

        if count_s1 == count_s2:
            return True

        for i in range(n1,n2):
            count_s2[ord(s2[i]) - 97] += 1
            count_s2[ord(s2[i - n1]) - 97] -= 1

            if count_s1 == count_s2:
                return True
        return False


# Q242
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False
        
        n1 = len(s)
        n2 = len(t)

        if n1 != n2:
            return False

        count_s = [0] * 26
        count_t = [0] * 26
        
        for i in range(n1):
            count_s[ord(s[i]) - 97] += 1
            count_t[ord(t[i]) - 97] += 1
        
        if count_s == count_t:
            return True
        else:
            return False

# Q49
# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagram_dict = defaultdict(list)
    
#         for words in strs:
#             count = [0] * 26
#             for char in words:
#                 count[ord(char) - 97] += 1  # a--> 1, b--> 2

#             key = tuple(count)
#             anagram_dict[key].append(words)
#         return list(anagram_dict.values())

# Q9
class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = str(x)
        left_pointer = 0
        right_pointer = len(res) - 1
        while left_pointer < right_pointer:
            if res[left_pointer] != res[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -=1
        return True
        

# Q7
class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0  # True or False
        x = abs(x)
        reversed_number = 0
        while x > 0:
            reversed_number = reversed_number * 10 + (x % 10)  # % --> remainder
            x = x // 10   # //  --> round off value

        if is_negative:
            reversed_number = -(reversed_number)
        
        if reversed_number < -2**31 or reversed_number > 2**31 - 1:
            return 0
        
        return reversed_number

        
