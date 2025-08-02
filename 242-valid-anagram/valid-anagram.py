class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        s_char_dictionary = {}
        t_char_dictionary = {}

        for ch in s:
            if ch not in s_char_dictionary:
                s_char_dictionary[ch] = 1
            else:
                s_char_dictionary[ch] += 1

        for ch in t:
            if ch not in t_char_dictionary:
                t_char_dictionary[ch] = 1
            else:
                t_char_dictionary[ch] += 1

        if t_char_dictionary != s_char_dictionary:
            return False
        else:
            return True