class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        #adjList -> undirected edges
        adjList = [[] for _ in range(n)]
        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        #complete adjList
        visited =[False] *n
        def dfs(node):
            for nei in adjList[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        res = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                res += 1
        return res
