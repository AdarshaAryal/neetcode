class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adjacency_list = collections.defaultdict(list)
        for source, destination, weight in edges:
            adjacency_list[source].append((weight, destination))
        
        heap = [(0, src)]
        visited = {}
        while heap:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited[node] = weight
            for neighbour_weight, neighbour in adjacency_list[node]:
                next_weight = weight + neighbour_weight

                heapq.heappush(heap, (next_weight, neighbour))
        
        for node_number in range(n):
            if node_number not in visited:
                visited[node_number] = -1
        
        return visited

