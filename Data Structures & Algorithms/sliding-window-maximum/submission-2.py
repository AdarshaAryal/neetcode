class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(heap)
        res = [-heap[0][0]]
        for i in range(k, len(nums)):
            while heap and (i - heap[0][1]) >= k:
                heapq.heappop(heap)
            heapq.heappush(heap, (-nums[i], i))
            res.append(-heap[0][0])

        return res 
