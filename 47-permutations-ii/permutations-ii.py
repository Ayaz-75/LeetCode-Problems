class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return nums
        # [1,2,3] -> [2,1,3] -> [2,3,1] => res[[2,3,1]]
        # [2,1,3] -> 
        res = []

        def backtrack(start):
            if start == len(nums):
                res.append(nums.copy())
                return

            seen = set()
            for i in range(start, len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    nums[i], nums[start] = nums[start], nums[i]
                    backtrack(start+1)
                    nums[start], nums[i] = nums[i], nums[start]
        backtrack(0)
        return res