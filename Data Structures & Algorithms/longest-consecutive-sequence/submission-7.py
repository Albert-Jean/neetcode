class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num - 1) not in numSet:
                l = 1
                while (num+l) in numSet:
                    l += 1
                longest = max(l,longest)           
        return longest
               

        