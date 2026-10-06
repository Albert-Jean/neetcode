class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])
        visited = set()
        queue = deque()
        #add all treasures to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    queue.append((r,c))
                    visited.add((r,c))
            
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                length = 0
                #set neighbors directions
                neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in neighbors:
                    length+=1
                    #check if oob or visited or blocked
                    if(min(r+dr,c+dc)<0
                    or r+dr == rows
                    or c+dc == cols
                    or (r+dr,c+dc) in visited
                    or grid[r+dr][c+dc] == -1):
                        continue
                    visited.add((r+dr,c+dc))
                    queue.append((r+dr,c+dc))
                    grid[r+dr][c+dc] = grid[r][c]+1
                    
        