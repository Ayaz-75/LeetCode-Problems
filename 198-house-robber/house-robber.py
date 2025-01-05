class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self.helper(nums, 0, memo)

    def helper(self, nums, idx, memo):
        # Base case
        if idx >= len(nums):
            return 0
        # Check memo
        if idx in memo:
            return memo[idx]
        # Compute result and store in memo
        memo[idx] = max(nums[idx] + self.helper(nums, idx + 2, memo), self.helper(nums, idx + 1, memo))
        return memo[idx]

        


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         return self.helper(nums, 0)
#     def helper(self, nums, idx):
#         if idx >= len(nums):
#             return 0
#         return max(nums[idx] + self.helper(nums, idx + 2), self.helper(nums, idx + 1))


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         return rob(nums, 0)

#     def rob(nums, idx):
#         if idx >= len(nums):
#             return 0
#         return max(nums[idx] + rob(nums, idx + 2), rob(nums, idx + 1))

