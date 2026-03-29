class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = collections.defaultdict(list)
        
        for s,d, weight in edges:
            adj[s].append([d, weight])
        
        shortest = {}
        min_heap = [(0, src)]

        distances = collections.defaultdict(lambda: float('inf'))
        distances[src] = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    new_dist = w1 + w2
                    if new_dist < distances[n2]:
                        distances[n2] = new_dist
                        heapq.heappush(min_heap, (new_dist, n2))
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        
        return shortest
