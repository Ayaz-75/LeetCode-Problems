class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        while b:
            carry = (a & b) & MASK  # Calculate carry
            a = (a ^ b) & MASK      # Sum without carry
            b = carry << 1          # Shift carry left
    
        return a if a <= INT_MAX else ~(a ^ MASK)
    