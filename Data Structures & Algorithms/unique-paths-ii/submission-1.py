class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[0] * (cols) for _ in range(rows)]
        print(cache)
        def dp(r, c, grid, cache):
            if r == rows or c == cols or grid[r][c] == 1:
                return 0
            if cache[r][c] != 0:
                return cache[r][c]
            if r == rows - 1 and c == cols - 1:
                return 1
            cache[r][c] = dp(r + 1, c, grid, cache) + dp(r, c + 1, grid, cache)
            return cache[r][c]

        return dp(0, 0, obstacleGrid,cache)

        