class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:    
        heapq.heapify(nums)
        k = len(nums)-k
        res = nums[0]
        while k > 0:
            if nums:
                heapq.heappop(nums)
            k -= 1
        return nums[0]

        