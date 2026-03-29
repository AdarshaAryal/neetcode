class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N
        prefix = [1] * N
        suffix = [1] * N

        for i in range(1, N):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        for i in range(N -2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        
        for i in range(N):
            res[i] = prefix[i] * suffix[i]
        
        return res