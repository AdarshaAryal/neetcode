class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        LAND, WATER = "1", "0"
        LENGTH, WIDTH = len(grid), len(grid[0])
        seen = set()
        direction = [(1,0), (0,1), (-1,0), (0, -1)]

        res = 0

        def is_valid(x,y):
            if (0 <= x < LENGTH) and (0 <= y < WIDTH) and (x, y) not in seen and grid[x][y] == LAND:
                return True
            return False 

        def dfs(x, y):
            for dx, dy in direction:
                cur_x, cur_y = x + dx, y + dy
                if is_valid(cur_x, cur_y):
                    seen.add((cur_x, cur_y))
                    dfs(cur_x, cur_y)
            return 
        
        for r in range(LENGTH):
            for c in range(WIDTH):
                if is_valid(r,c):
                    res += 1
                    seen.add((r, c))
                    dfs(r, c)
        
        return res


