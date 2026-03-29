class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjacency_list = collections.defaultdict(list)
        for edge1, edge2, weight in edges:
            adjacency_list[edge1].append((weight, edge2))
            # adjacency_list[edge2].append((weight, edge1))
        
        visited = set()
        heap = [(0, src)] # weight, node
        res = {}
        while heap:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
            res[node] = weight
            visited.add(node)

            for edge_weight, edge in adjacency_list[node]:
                if edge in visited:
                    continue
                heapq.heappush(heap, (weight+edge_weight, edge))
        
        for i in range(n):
            if i not in res:
                res[i] = -1
        
        return res




