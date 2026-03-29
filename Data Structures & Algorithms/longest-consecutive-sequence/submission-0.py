class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for num in nums:
            start = num
            cur_len = 0
            while start in nums_set:
                start += 1
                cur_len += 1
            max_len = max(max_len, cur_len)
        
        return max_len