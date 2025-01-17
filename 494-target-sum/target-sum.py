class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        # If the target is not reachable, return 0
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0
        subset_sum = (total_sum + target) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[subset_sum]


# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         def dfs(index, current_sum):
#             if index == len(nums):
#                 return 1 if current_sum == target else 0
            
#             add = dfs(index + 1, current_sum + nums[index])
#             subtract = dfs(index + 1, current_sum - nums[index])
            
#             return add + subtract
        
#         return dfs(0, 0)