class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            if num not in arr:
                arr.append(num)
            else:
                arr.remove(num)
        return arr[0]