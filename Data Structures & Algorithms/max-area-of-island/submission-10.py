class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visited = set()
        maxArea =  0
        def dfs(grid,r,c,visited):
            #base case : value is incorect return 0 -> out of bound, in visited ?
            #add current r,c to visited
            #area +=1 
            #dfs all directions
            if r<0 or r==rows or c < 0 or c == cols or (r,c) in visited or grid[r][c]==0:
                return 0
            visited.add((r,c))
            return 1 + dfs(grid,r+1,c,visited) + dfs(grid,r-1,c,visited) + dfs(grid,r,c+1,visited) + dfs(grid,r,c-1,visited)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==1 and (r,c) not in visited:
                    #run dfs
                    area = dfs(grid,r,c,visited)
                    maxArea = max(area,maxArea)
        return maxArea