class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #constants
        rows, cols = len(grid), len(grid[0])  
        q = deque()           
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]   
        fresh = 0
        time = 0
        #find rotten fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c]==2:
                    q.append((r,c))
        # bfs multi start
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in neighbors:
                    new_r, new_c = r + dr, c + dc
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        q.append((new_r, new_c))
            time += 1
    
        return time if fresh == 0 else -1
