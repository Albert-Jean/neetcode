import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []     
        for i in range(len(nums)):
            if stack:
                if nums[i] > stack[-1]:
                    stack.append(nums[i])
                else:
                    idx = bisect.bisect_left(stack, nums[i])
                    stack[idx] = nums[i]

            else:
                stack.append(nums[i])
        return len(stack)