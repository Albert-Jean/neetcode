class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols = len(matrix),len(matrix[0])
        ORows = [False] * rows
        OCols = [False] * cols
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    ORows[r] = True
                    OCols[c] = True
        
        for r in range(rows):
            for c in range(cols):
                if ORows[r] or OCols[c]:
                    matrix[r][c] =0


        
        