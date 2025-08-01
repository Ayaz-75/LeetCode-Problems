class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        counter = 0
        new_nums = []
        i = 0
        while i < len(nums):
            counter += nums[i]
            new_nums.append(counter)
            i += 1

        return new_nums