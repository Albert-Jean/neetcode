class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            #compute distance
            computedDist = points[i][0]**2 + points[i][1]**2
            heap.append((computedDist, points[i]))
        heapq.heapify(heap)
        res = []
        for j in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
