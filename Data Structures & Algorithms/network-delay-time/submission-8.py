class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList={}
        for i in range(1,n+1):
            adjList[i] = []
        for u,v,w in times:
            adjList[u].append([v,w])
        minHeap = [(0, k)]
        shortest = {}
        while minHeap:
            w1, s1 = heapq.heappop(minHeap)
            if s1 in shortest:
                continue
            shortest[s1] = w1

            for s2,w2 in adjList[s1]:
                    heapq.heappush(minHeap, (w1+w2, s2))
        return max(shortest.values()) if len(shortest) == n else -1
            