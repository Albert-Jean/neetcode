class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:    
        minHeap=nums[::]
        heapq.heapify(minHeap)       
        while len(minHeap) >=k:
            res = heapq.heappop(minHeap)
        return res
        