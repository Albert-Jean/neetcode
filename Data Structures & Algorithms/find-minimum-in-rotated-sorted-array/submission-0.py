class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = 1000
        for n in nums:
            if n < mini:
                mini = n 
        return mini 

        