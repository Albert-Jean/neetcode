class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visited = set()
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([r,c])
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        res=0
        while queue and fresh > 0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                nei = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in nei:
                    new_r = r+dr
                    new_c = c+dc
                    if (new_r<0 or new_r == rows or new_c<0 or new_c == cols or
                    (new_r,new_c) in visited or 
                    grid[new_r][new_c]!=1):
                        continue
                    grid[new_r][new_c] = 2
                    fresh -= 1
                    queue.append([new_r,new_c])
                    visited.add((new_r,new_c))
            res += 1
        return res if fresh == 0 else -1