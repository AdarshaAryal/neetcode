class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            if (num - 1) not in nums_set:
                start = 0
                while (num + start) in nums_set:
                    start += 1
                res = max(res, start)
        
        return res