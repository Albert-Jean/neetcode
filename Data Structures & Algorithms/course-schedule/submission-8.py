class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for dst,src in prerequisites:
            adj[src].append(dst)
        #----------------------------------------

        visited = set()
        cycle = set()
        topSort = []
        def dfs(src,adj,visited,cycle):
            if src in visited:
                return True
            if src in cycle:
                return False
            cycle.add(src)
            for nei in adj[src]:
                if not dfs(nei,adj,visited,cycle):
                    return False
            visited.add(src)
            cycle.remove(src)
            return True
        for i in range(numCourses):
            if not dfs(i,adj,visited,cycle):
                return False
        return True
        