class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        
        char_count = Counter(s)
        length = 0
        odd_found = False
        
        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True
        
        if odd_found:
            length += 1
        
        return length

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def expandAroundCenter(left: int, right: int) -> str:
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             return s[left + 1:right]

#         longest = ""
#         for i in range(len(s)):
#             palindrome1 = expandAroundCenter(i, i)
#             palindrome2 = expandAroundCenter(i, i + 1)
#             if len(palindrome1) > len(longest):
#                 longest = palindrome1
#             if len(palindrome2) > len(longest):
#                 longest = palindrome2
        
#         return longest


        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #     return s[left + 1:right]

        # longest = ""
        # for i in range(len(s)):
        #     palindrome1 = expandAroundCenter(i, i)
        #     palindrome2 = expandAroundCenter(i, i + 1)
        #     longest = max(longest, palindrome1, palindrome2, key=len)
        
        # return len(longest)
