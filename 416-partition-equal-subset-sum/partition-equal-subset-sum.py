class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is odd, partitioning is impossible
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True  # Base case
        
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]