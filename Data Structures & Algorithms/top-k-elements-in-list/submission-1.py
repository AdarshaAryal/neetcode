class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements_counter = collections.Counter(nums)
        heap = [(-val, key_) for key_, val in elements_counter.items()]
        heapq.heapify(heap)

        res = []
        for i in range(k):
            _, key_ = heapq.heappop(heap)
            res.append(key_)

        return res   