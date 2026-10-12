class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        #combine edges with succProb
        my_tuple = []
        for i in range(len(edges)):
            my_tuple.append((edges[i][0],edges[i][1],succProb[i]))
        #build adjList src,dst,prob
        adjList = {}
        for i in range(n):
            adjList[i] =[]
        for s,d,w in my_tuple:
            adjList[s].append((d,w))
            adjList[d].append((s,w))
        shortest = {}
        maxHeap = [(-1.0,start_node)]
        while maxHeap:
            w1,n1 = heapq.heappop(maxHeap)
            if n1 in shortest:
                continue
            shortest[n1]=w1
            if n1 == end_node:
                return -w1
            for n2,w2 in adjList[n1]:
                if n2 not in shortest:
                    heapq.heappush(maxHeap, (w1 * w2, n2))
        return 0.0