class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        orig_color = image[sr][sc]
        if orig_color == color:
            return image
        def dfs(r,c):
            #Base case 1 : Out of bound or not valid do nothing
            if r<0 or r>=rows or c<0 or c>=cols or image[r][c]!=orig_color:
                return 
            #Base case 2: else change color
            image[r][c]=color

            #recursion 
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
        
        dfs(sr,sc)
        return image


        