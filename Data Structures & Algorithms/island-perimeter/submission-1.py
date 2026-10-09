class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        visited = set()
        def dfs(grid,r,c,visited):
            if r<0 or r==rows or c<0 or c == cols or grid[r][c] == 0:
                return 1
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            return (dfs(grid,r+1,c,visited) +
                    dfs(grid,r-1,c,visited) +
                    dfs(grid,r,c+1,visited) +
                    dfs(grid,r,c-1,visited))
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    return dfs(grid,r,c,visited)
        return 0