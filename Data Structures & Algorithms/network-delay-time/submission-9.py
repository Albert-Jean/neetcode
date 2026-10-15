class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        for s,d,w in times:
            adj[s].append((d, w))
        
        minHeap = [(0, k)]
        shortest = {}
        while minHeap:
            w1, s1 = heapq.heappop(minHeap)
            if s1 in shortest:
                continue
            shortest[s1] = w1
            for s2, w2 in adj[s1]:
                heapq.heappush(minHeap, (w1 + w2, s2))
        return -1 if len(shortest) != n else max(shortest.values())