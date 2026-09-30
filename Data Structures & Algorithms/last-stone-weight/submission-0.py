class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #build maxHeap -> heapify algo
        #x,y=maxHeap[0],maxHeap[1]
        #if x==y pop from heap 0 and 1
        #x<y pop x and y  / new val=y-x -> insert y into heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) >1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones,first - second)
        stones.append(0)
        return abs(stones[0])
        