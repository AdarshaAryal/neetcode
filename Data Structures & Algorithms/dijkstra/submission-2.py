class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        adjacency_list = collections.defaultdict(list)
        for u,v, weight in edges:
            adjacency_list[u].append((weight, v))
        
        shortest = {}
        min_distance = collections.defaultdict(lambda: float('inf'))
        min_heap = [(0, src)] # min_distance, source

        while min_heap:
            dist, node = heapq.heappop(min_heap)
            if node in shortest:
                continue
            shortest[node] = dist
            for weight, neighbor in adjacency_list[node]:
                if neighbor not in shortest:
                    cur_weight = weight+dist
                    if min_distance[neighbor] > cur_weight:
                        min_distance[neighbor] = cur_weight
                        heapq.heappush(min_heap, (weight+dist, neighbor))
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        
        return shortest


