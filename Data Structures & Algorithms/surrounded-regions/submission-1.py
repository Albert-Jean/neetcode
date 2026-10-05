class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board),len(board[0])
        border = set()

        for c in range(cols):
            if board[0][c] == "O":
                border.add((0, c))

            if board[rows - 1][c] == "O":
                border.add((rows - 1, c))
        # Left and right columns
        for r in range(rows):
            if board[r][0] == "O":
                border.add((r, 0))

            if board[r][cols - 1] == "O":
                border.add((r, cols - 1))
        
        def dfs(r,c):
            #Base case 1: out of bound or board[r][c] != 'O' -> do nothing
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r, c in border:
            dfs(r, c)
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
