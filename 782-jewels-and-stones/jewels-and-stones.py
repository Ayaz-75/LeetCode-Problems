class Solution:
    def numJewelsInStones(self, jw: str, st: str) -> int:
        jewel_set = set(jw)
        count = 0
        
        for stone in st:
            if stone in jewel_set:
                count += 1
        
        return count
