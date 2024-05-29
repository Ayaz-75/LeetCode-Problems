class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Step 1: Trim the string to remove leading and trailing spaces
        trimmed_str = s.strip()
        
        # Step 2: Split the trimmed string into a list of words
        words = trimmed_str.split()
        
        # Step 3: Return the length of the last word in the list
        if words:
            return len(words[-1])
        else:
            return 0
