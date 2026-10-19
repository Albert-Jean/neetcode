class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj={}
        for i in range(1, n + 1):
            adj[i] = []
        for src,dst,time in times:
            adj[src].append((dst,time))

        minHeap=[(0,k)]
        shortest ={}
        t=0
        while minHeap:
            time1,src1= heapq.heappop(minHeap)
            if src1 in shortest:
                continue
            shortest[src1] = time1
            t=time1
            for src2,time2 in adj[src1]:
                heapq.heappush(minHeap,(time1+time2,src2))
        return - 1 if len(shortest) != n else t
