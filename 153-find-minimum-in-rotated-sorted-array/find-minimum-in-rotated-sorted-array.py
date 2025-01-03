class Solution:
    def findMin(self, nums: List[int]) -> int:
    
        leftPart = 0
        rightPart = len(nums) - 1

        while leftPart < rightPart:
            mid = (leftPart + rightPart) // 2

            if nums[mid] <= nums[rightPart]:
                rightPart = mid
            else:
                leftPart = mid + 1
        
        return nums[leftPart]