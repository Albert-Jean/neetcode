class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        #dfs statrting from every pac and atlantic border
        #keep a set of all cell that flow to pacific -> same for atlantic
        #check if (r,c) in both set 
        rows,cols = len(heights),len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(heights,r,c,visited,prevHeight):
            if r<0 or r==rows or c <0 or c==cols or (r,c) in visited or heights[r][c] < prevHeight:
                return
            visited.add((r,c))
            dfs(heights,r+1,c,visited,heights[r][c])
            dfs(heights,r-1,c,visited,heights[r][c])
            dfs(heights,r,c+1,visited,heights[r][c])
            dfs(heights,r,c-1,visited,heights[r][c])            

        for r in range(rows):
            #run dfs on first and last col
            dfs(heights,r,0,pacific,heights[r][0])
            dfs(heights,r,cols-1,atlantic,heights[r][cols-1])
        for c in range(cols):
            dfs(heights,0,c,pacific,heights[0][c])
            dfs(heights,rows-1,c,atlantic,heights[rows-1][c])
        
        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res


        