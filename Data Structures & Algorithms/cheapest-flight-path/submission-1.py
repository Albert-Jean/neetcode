class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for f, d, c in flights:
            adj[f].append([d, c])
        
        # minHeap entries: (cost, node, stops)
        minHeap = [(0, src, 0)]
        # Track the minimum stops taken to reach each node
        min_stops = {}
        
        while minHeap:
            cost, node, stops = heapq.heappop(minHeap)
            if node == dst:
                return cost
            if stops > k:
                continue
            if node in min_stops and min_stops[node] <= stops:
                continue
            min_stops[node] = stops
            
            for neighbor, price in adj[node]:
                heapq.heappush(minHeap, (cost + price, neighbor, stops + 1))
                
        return -1