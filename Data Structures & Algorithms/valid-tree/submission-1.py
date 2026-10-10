class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for src,dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        if len(edges) > n-1:
            return False

        def dfs(src,par):
            if src in visited:
                return False
            visited.add(src)
            for nei in adjList[src]:
                if nei == par:
                    continue
                if not dfs(nei,src):
                    return False
            return True
        #topological Sort algorithm
        visited = set()
        return dfs(0,-1) and len(visited) == n 
        