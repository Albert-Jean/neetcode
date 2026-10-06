class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visited = set()
        queue = deque()
        #add all rotten fruit to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
                    visited.add((r,c))
        
        timer = 0

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in neighbors:
                    #check if out of bound or visited or blocked
                    if(min(r+dr,c+dc)<0
                    or r+dr == rows
                    or c+dc == cols
                    or (r+dr,c+dc) in visited
                    or grid[r+dr][c+dc] == 0):
                        continue
                    #append queue add visited
                    queue.append((r+dr,c+dc))
                    visited.add((r+dr,c+dc))
                    grid[r+dr][c+dc] = 2
            if queue:
                timer += 1

        if not self.checkFreshFruit(grid,rows,cols):
            return timer
        return -1
                

    def checkFreshFruit(self,grid,rows,cols)->bool:
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return True
        return False
