class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for src,dst in prerequisites:
            adj[src].append(dst)
        #----------------------------------------

        visited = set()
        cycle = set()
        topSort = []
        def dfs(src,adj,visited,cycle,topSort):
            if src in visited:
                return True
            if src in cycle:
                return False
            cycle.add(src)
            for nei in adj[src]:
                if not dfs(nei,adj,visited,cycle,topSort):
                    return False
            topSort.append(src)
            visited.add(src)
            cycle.remove(src)
            return True
        for i in range(numCourses):
            if not dfs(i,adj,visited,cycle,topSort):
                return[]
        return topSort
        