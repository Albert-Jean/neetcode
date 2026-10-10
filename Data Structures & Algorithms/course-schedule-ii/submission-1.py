class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #topological sort 
        #dfs with cycle detection 
        def dfs(src,adjList,visited,topSort,path):
            if src in path:
                return False
            if src in visited:
                return True
            path.add(src)
            visited.add(src)
            for nei in adjList[src]:
                if not dfs(nei,adjList,visited,topSort,path):
                    return False
            path.remove(src)
            topSort.append(src)
            return True
        #build adjList
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for src,dst in prerequisites:
            adjList[src].append(dst)
        
        #make topologicalSort
        topSort = []
        visited = set()      
        path = set()
        for i in range(numCourses):
            if dfs(i,adjList,visited,topSort,path):
                continue
            else:
                return []   
        return topSort
