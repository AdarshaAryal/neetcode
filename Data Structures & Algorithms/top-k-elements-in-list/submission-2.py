class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements_counter = collections.Counter(nums) # T: O(n), S: O(n)
        # elements_counter = {1:1, 2: 2, 3:3}
        heap = [(val, key_) for key_, val in elements_counter.items()] # T: O(n), S: O(n)
        # heap = [(-1, 1), (-2, 2), (-3, 3)]
        res = [] 
        # res = []
        for h in heap: # h = (-3, 3)
            if len(res) >= k: # 
                heapq.heappushpop(res, h) # res = [(-2, 2), (-3, 3)]
            else:
                heapq.heappush(res, h) # res = [(-1, 1), (-2, 2), ]
        
        return list(r[1] for r in res)
