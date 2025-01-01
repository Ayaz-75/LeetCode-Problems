class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inds = []
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    inds.append(i)
                    inds.append(j)
        return inds