class Solution:
    def climbStairs(self, n: int) -> int:
        #fibonacci problem
        #top-down approach
        #base case : 1 stair -> 1 way 2 stairs -> 2 ways
        cache = {}
        def helper(n,cache):
            if n in cache:
                return cache[n]            
            if n <=2:
                return n 
            cache[n] = helper(n-1,cache) + helper(n-2,cache)
            return cache[n]
        return helper(n,cache)
        