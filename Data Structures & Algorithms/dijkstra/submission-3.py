class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjacency_list = collections.defaultdict(list)
        for s, d, w in edges:
            adjacency_list[s].append((d, w))
        
        res = {}
        min_heap = [(0, src)] # weight, node

        while min_heap:
            cur_weight, node = heapq.heappop(min_heap)
            if node in res:
                continue
            res[node] = cur_weight
            for dest, weight in adjacency_list[node]:
                if dest in res:
                    continue
                heapq.heappush(min_heap, (weight+cur_weight, dest))
        
        for i in range(n):
            if i not in res:
                res[i] = -1
        
        return res
