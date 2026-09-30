class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l,r = 1 , n-1
        while(l < r):
            twosum = l + r
            if twosum > target:
                r -= 1
            if twosum < target:
                l += 1
            else:
                return [l,r]
        return [-1,-1]
