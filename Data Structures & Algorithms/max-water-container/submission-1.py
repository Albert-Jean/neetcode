class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        maxArea = 0
        while l<r:
            maxArea = max(maxArea, min(heights[l],heights[r])*(r-l))
            l+=1
        return maxArea

        