class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProd = [1] * n
        rightProd = [1] * n
        result = [0] * n

        for i in range(1, n):
            leftProd[i] = leftProd[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            rightProd[i] = rightProd[i + 1] * nums[i + 1]

        for i in range(n):
            result[i] = leftProd[i] * rightProd[i]

        return result

        # n = len(nums)
        # leftProd = [0] * n
        # rightProd = [0] * n
        # result = [0] * n

        # # leftProd[0] = 1
        # for i in range(1, n):
        #     leftProd[i] = leftProd[i-1] * nums[i-1]
        
        # # rightProd[n-1] = 1
        # for i in range(n-2, -1, -1):
        #     rightProd[i] = rightProd[i + 1] * nums[i + 1]

        # for i in range(n):
        #     result[i] = leftProd[i] * rightProd[i]

        # return result