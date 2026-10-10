class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for src,dst in prerequisites:
            adjList[src].append(dst)

        def dfs(src,adjList,visited,cycle):
            if src in cycle:
                return False
            if src in visited:
                return True

            cycle.add(src)
            
            for nei in adjList[src]:
                if not dfs(nei,adjList,visited,cycle):
                    return False
            cycle.remove(src)
            visited.add(src)
            return True
        #topological Sort algorithm
        visited = set()
        cycle =set()
        for i in range(numCourses):
            if not dfs(i,adjList,visited,cycle):
                return False
        return True

        