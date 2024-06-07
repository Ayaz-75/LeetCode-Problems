class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        # Create a table to store the minimum jumps required to reach each index
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n):
            max_reach = min(i + nums[i], n - 1)
            for j in range(i + 1, max_reach + 1):
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[-1]
