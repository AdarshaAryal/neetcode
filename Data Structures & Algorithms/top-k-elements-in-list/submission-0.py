class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = collections.Counter(nums)
        bucket_sort = [0]*(len(nums) + 1)

        for num, freq in nums_counter.items():
            if bucket_sort[freq] == 0:
                bucket_sort[freq] = [num]
            else:
                bucket_sort[freq].append(num)
        
        res = []
        
        for i in range(len(bucket_sort)-1, -1, -1):
            if bucket_sort[i] != 0:
                res.extend(bucket_sort[i])
            if len(res) == k:
                break
        
        return res