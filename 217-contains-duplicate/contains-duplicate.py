class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[i] == nums[j]:
        #             return True
        #         return False
