from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        
        if n <= 1:
            return
        
        # Step 1: Find the first decreasing element from the end
        partition_ind = n - 2
        while partition_ind >= 0 and nums[partition_ind] >= nums[partition_ind + 1]:
            partition_ind -= 1
        
        # If the entire array is in descending order
        if partition_ind == -1:
            nums.reverse()
            return
        
        # Step 2: Find the element just larger than nums[partition_ind] from the end
        for i in range(n - 1, partition_ind, -1):
            if nums[i] > nums[partition_ind]:
                # Step 3: Swap the found element with the partition index element
                nums[partition_ind], nums[i] = nums[i], nums[partition_ind]
                break
        
        # Step 4: Reverse the sequence after the partition index
        self.reverseArrayPartially(nums, partition_ind + 1, n - 1)
    
    def reverseArrayPartially(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
