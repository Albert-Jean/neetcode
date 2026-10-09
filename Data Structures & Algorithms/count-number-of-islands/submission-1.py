class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        visited =set()
        islands = 0
        
        def dfs(grid,r,c,visited):
            if r>=rows or r<0 or c>=cols or c<0 or (r,c) in visited:
                return
            if grid[r][c] == "0":
                return
            visited.add((r,c))

            dfs(grid,r+1,c,visited)
            dfs(grid,r-1,c,visited)
            dfs(grid,r,c+1,visited)
            dfs(grid,r,c-1,visited)
            return 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(grid,r,c,visited)
                    islands+=1
                                       
        return islands