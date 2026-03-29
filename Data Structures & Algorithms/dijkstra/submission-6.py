class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjacency_list = collections.defaultdict(list)
        for edge1, edge2, weight in edges:
            adjacency_list[edge1].append((weight, edge2))
        

        heap = [(0, src)] # weight 0, starting vertex
        visited = set()
        res = {}
        while heap:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            res[node] = weight

            for neighbour_weight, neighbour in adjacency_list[node]:
                if neighbour not in visited:
                    heapq.heappush(heap, (weight + neighbour_weight, neighbour))

        for i in range(n):
            if i not in res:
                res[i] = -1
        
        return res