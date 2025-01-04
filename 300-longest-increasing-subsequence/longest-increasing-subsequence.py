class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)
                sub[idx] = x
        return len(sub)

# ----- Works just in time not exceeding the time limit. ----- #

        # def helper(ind, prev):
        #     if ind == len(nums):
        #         return 0
            
        #     # Option 1: Do not take the current element
        #     notake = helper(ind + 1, prev)
            
        #     # Option 2: Take the current element (if valid)
        #     take = 0
        #     if prev == -1 or nums[ind] > nums[prev]:
        #         take = 1 + helper(ind + 1, ind)
            
        #     return max(notake, take)
        
        # return helper(0, -1)


# ------Exceeds the time limit ------ #
        # n = len(nums)
        # mem = [[-1] * (n + 1) for _ in range(n + 1)]    
        # def helper(ind, prev):
        #     if ind == len(nums):
        #         return 0
        #     if mem[ind][prev + 1] != -1:
        #         return mem[ind][prev + 1]
        #     notake = helper(ind + 1, prev)
        #     take = 0
        #     if prev == -1 or nums[ind] > nums[prev]:
        #         take = 1 + helper(ind + 1, ind)

        #     mem[ind][prev + 1] = max(notake, take)
        #     return mem[ind][prev + 1]
        
        # return helper(0, -1)
