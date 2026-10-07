class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,cols = len(board),len(board[0])
        #duplicate in rows
        for r in range(rows):
            dupSet = set()
            for c in range(cols) :
                if board[r][c] != '.':
                    if board[r][c] in dupSet:
                        return False
                    dupSet.add(board[r][c])
       #duplicate in cols
        for c in range(cols):
            dupSet = set()
            for r in range(rows):
                if board[r][c] != '.':
                    if board[r][c] in dupSet:
                        return False
                    dupSet.add(board[r][c])
        #duplicate in square
        #9 3*3 squares 
        for square in range(9):
            dupSet = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3+i
                    col = (square%3) * 3+j
                    if board[row][col] != ".":
                        if board[row][col] in dupSet:
                            return False
                        dupSet.add(board[row][col])
        return True
