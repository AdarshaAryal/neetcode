class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,2,4,6]
        # left_prd = [1] * len(nums), right_prd = [1] * len(nums)
        # res[n] = left_prd[n-1] * right_prd[n+1]

        N = len(nums)
        left_prd = [1] * N
        left_prd[0] = nums[0]
        right_prd = [1] * N
        right_prd[-1] = nums[-1]

        for i in range(1, N):
            left_prd[i] = left_prd[i-1]*nums[i]
        
        for j in range(N-2, -1,-1):
            right_prd[j] = right_prd[j+1] * nums[j]
        
        res = [1] * N
        for i in range(N):
            left_val = left_prd[i-1] if i -1 >= 0 else 1
            right_val = right_prd[i+1] if i + 1 < N else 1
            res[i] = left_val * right_val
        
        return res
        
        

