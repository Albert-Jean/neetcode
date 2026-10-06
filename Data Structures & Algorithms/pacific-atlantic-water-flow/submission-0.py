class Solution:
        def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

            rows, cols = len(heights), len(heights[0])

            pacific = set()
            atlantic = set()

            def dfs(r, c, visited, prev_height):
                # Invalid cell, already visited, or cannot move uphill
                if (
                    r < 0 or r >= rows or
                    c < 0 or c >= cols or
                    (r, c) in visited or
                    heights[r][c] < prev_height
                ):
                    return

                visited.add((r, c))
                current_height = heights[r][c]

                dfs(r + 1, c, visited, current_height)
                dfs(r - 1, c, visited, current_height)
                dfs(r, c + 1, visited, current_height)
                dfs(r, c - 1, visited, current_height)

            # Start DFS from Pacific borders
            for r in range(rows):
                dfs(r, 0, pacific, heights[r][0])

            for c in range(cols):
                dfs(0, c, pacific, heights[0][c])

            # Start DFS from Atlantic borders
            for r in range(rows):
                dfs(r, cols - 1, atlantic, heights[r][cols - 1])

            for c in range(cols):
                dfs(rows - 1, c, atlantic, heights[rows - 1][c])

            # Cells reachable from both oceans
            result = []

            for r in range(rows):
                for c in range(cols):
                    if (r, c) in pacific and (r, c) in atlantic:
                        result.append([r, c])

            return result
            
    
            