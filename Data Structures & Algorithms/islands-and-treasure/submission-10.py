class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols =  len(grid), len(grid[0])
        visited = set()
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r,c))
        
        dis = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = dis
                neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in neighbors:
                    new_r = r + dr
                    new_c = c + dc
                    if new_r < 0 or new_r == rows or new_c < 0 or new_c == cols or (new_r,new_c) in visited or grid[new_r][new_c] == -1:
                        continue                        
                    visited.add((new_r,new_c))
                    queue.append([new_r,new_c])
            dis +=1
