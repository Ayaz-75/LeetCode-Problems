class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0] 
        for i in range(len(nums)):
            curSum += nums[i]
            maxSum = max(maxSum, curSum)

            if curSum < 0: 
                curSum = 0
        return maxSum