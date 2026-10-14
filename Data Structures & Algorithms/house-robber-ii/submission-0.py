class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = {}
        def dfs(n,flag):
            if n >= len(nums) or (flag and n == len(nums) - 1):
                return 0
            if (n, flag) in cache:
                return cache[(n, flag)]
            cache[(n, flag)] = max(dfs(n + 1, flag), nums[n] + dfs(n + 2, flag))
            return cache[(n, flag)]
        return max(dfs(0,True),dfs(1,False))
