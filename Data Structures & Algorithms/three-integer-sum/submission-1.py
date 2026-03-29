class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # T: O(nlogn), S : O(1), nums = [-4, -1, -1, 0, 1, 2]
        left = 0
        N = len(nums) # N = 6
        res = []
        while left < (N - 2): # left = 1
            while left > 0 and left < N and nums[left] == nums[left-1]:
                left += 1
            mid = left + 1 # mid = 2
            right = N - 1 # right = 5
            while mid < right:
                cur_sum = nums[left] + nums[mid] + nums[right] # cur_sum = -1 -1 + 2 -> cur_sum = 0
                if cur_sum == 0:
                    res.append([nums[left], nums[mid], nums[right]])
                    mid += 1 
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid +=1
                elif cur_sum > 0:
                    right -= 1
                else:
                    mid += 1
            left += 1
        # left = 1
        return res
