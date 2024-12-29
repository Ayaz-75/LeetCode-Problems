from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curProd = 1
        maxProd = nums[0]

        for i in range(len(nums)):
            curProd *= nums[i]
            maxProd = max(maxProd, curProd)

            if curProd == 0:
                curProd = 1
                
        curProd = 1

        for i in range(len(nums) - 1, -1, -1):
            curProd *= nums[i]
            maxProd = max(maxProd, curProd)

            if curProd == 0:
                curProd = 1
        
        return maxProd
