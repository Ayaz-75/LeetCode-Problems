class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        charIndexMap = {}
        maxLength = 0
        left = 0

        for right in range(n):
            if s[right] in charIndexMap:
                # Update the left pointer to the next position after the last occurrence of s[right]
                left = max(left, charIndexMap[s[right]] + 1)
            
            # Update the latest index of the character s[right]
            charIndexMap[s[right]] = right
            
            # Calculate the length of the current window and update maxLength if needed
            maxLength = max(maxLength, right - left + 1)

        return maxLength
