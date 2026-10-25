class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        
        cache = [[-1] * m for _ in range(n)]
        
        def dp(s1, s2, i1, i2, cache):
            if i1 == len(s1) or i2 == len(s2):
                return 0
            if cache[i1][i2] != -1:
                return cache[i1][i2]
            if s1[i1] == s2[i2]:
                cache[i1][i2] = 1 + dp(s1, s2, i1 + 1, i2 + 1, cache)
            else:
                cache[i1][i2] = max(dp(s1, s2, i1 + 1, i2, cache), dp(s1, s2, i1, i2 + 1, cache))
            return cache[i1][i2]
        return dp(text1, text2, 0, 0, cache)