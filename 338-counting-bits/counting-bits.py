class Solution:
    def countBits(self, num: int) -> list[int]:
        res = [0] * (num + 1)
        
        for i in range(1, num + 1):
            if i & 1 == 0:
                res[i] = res[i >> 1]
            else:
                res[i] = res[i - 1] + 1
        
        return res
