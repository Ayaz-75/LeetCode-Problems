class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid is greater than its right neighbor, peak might be on the left
            if nums[mid] > nums[mid + 1]:
                right = mid
            # Otherwise, peak might be on the right
            else:
                left = mid + 1
        
        return left
