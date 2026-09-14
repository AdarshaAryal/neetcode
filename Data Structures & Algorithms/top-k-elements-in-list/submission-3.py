class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dictionary where key = number, value is the frequency
        # convert the dictionary into a list[tuple[str, str]], and then to a heap
        # first is the -frequency, second is the key, as Python uses min heap
        # while k > 0, add the key in to a result list
        # Time Complexity: O(n) -> Counter, O(n) -> heapq.heapify, O(klogn) for the loop and heappop, can be improved to O(klogk)
        # Space Complexity: O(n) -> Counter, O(1)-> inplace, O(1) for loop, O(k) for final
        # Total Time Complexity: O(n + klogn)
        # Total Space Complexity: O(n)
        # Bucket sort

        nums_counter = Counter(nums)
        nums_heap = [(-val, key) for key, val in nums_counter.items()]
        heapq.heapify(nums_heap)
        res = []
        while k > 0:
            _, key = heapq.heappop(nums_heap)
            res.append(key)
            k -= 1
        
        return res

    