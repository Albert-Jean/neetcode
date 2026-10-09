class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #dfs on edges -> find all valid 0 -> validSet()
        #for each cell on the grid if 0 not in valid replace with X
        
        rows,cols = len(board),len(board[0])
        valid= set()
        def dfs(board,r,c,valid):
            if r<0 or r==rows or c<0 or c==cols or board[r][c] =="X" or (r,c) in valid:
                return
            valid.add((r,c))
            dfs(board,r+1,c,valid)
            dfs(board,r-1,c,valid)
            dfs(board,r,c+1,valid)
            dfs(board,r,c-1,valid)

        for c in range(cols):
            dfs(board,0,c,valid)
            dfs(board,rows-1,c,valid)
        for r in range(rows):
            dfs(board,r,0,valid)
            dfs(board,r,cols-1,valid)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in valid:
                    board[r][c] = "X"
