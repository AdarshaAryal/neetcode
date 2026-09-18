class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        LAND, WATER = 1, 0
        LENGTH, WIDTH = len(grid), len(grid[0])
        seen = set()
        direction = [(1,0), (0,1), (-1,0), (0, -1)]

        def is_valid(x,y):
            return (0 <= x < LENGTH) and (0 <= y < WIDTH) and (x, y) not in seen and grid[x][y] == LAND

        def dfs(x, y):
            nonlocal area
            for dx, dy in direction:
                cur_x, cur_y = x + dx, y + dy
                if is_valid(cur_x, cur_y):
                    seen.add((cur_x, cur_y))
                    area += 1
                    dfs(cur_x, cur_y)
            return area 
        
        max_area = 0
        for r in range(LENGTH):
            for c in range(WIDTH):
                if is_valid(r,c):
                    seen.add((r, c))
                    area = 1
                    dfs(r,c)
                    max_area = max(max_area, area)
        
        return max_area

        # T: O(mn), each cell is visited only once
        # S: O(mn), seen set 


