import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []     
        for i in range(len(nums)):
            idx = bisect.bisect_left(stack, nums[i])
            if idx == len(stack):
                stack.append(nums[i])
            else:
                stack[idx] = nums[i]
        return len(stack)