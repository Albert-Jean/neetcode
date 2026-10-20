class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows,cols=len(matrix),len(matrix[0])
        #spiral order directions: right, down, left, up
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set()
        res=[]
        def dfs(matrix,r,c,dir_idx,visited):
            if r<0 or c<0 or r==rows or c==cols or (r,c) in visited:
                return False
            visited.add((r,c))
            res.append(matrix[r][c])
            for i in range(4):
                next_dir = (dir_idx + i) % 4
                dr, dc = directions[next_dir]
                if dfs(matrix, r + dr, c + dc, next_dir, visited):
                    break
            return True
        dfs(matrix,0,0,0,visited)
        return res