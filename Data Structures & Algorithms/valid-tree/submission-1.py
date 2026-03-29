class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj_list = collections.defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        

        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)

            for nei in adj_list[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
            
            return True
        
        return dfs(0, -1) and n == len(visited)
        