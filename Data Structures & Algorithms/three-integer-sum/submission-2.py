class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        left = 0
        res = []
        while left < (N - 2):
            while 0 < left < (N - 2) and nums[left] == nums[left - 1]:
                left += 1
            mid = left + 1
            right = N - 1

            while mid < right:
                cur_sum = nums[left] + nums[mid] + nums[right]
                if cur_sum == 0:
                    res.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    mid += 1
            
            left += 1
    
        return res