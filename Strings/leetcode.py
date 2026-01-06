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
        
        