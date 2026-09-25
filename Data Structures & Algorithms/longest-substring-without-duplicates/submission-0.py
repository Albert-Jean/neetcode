class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        total = 0 
        hashSet = set()
        res=0
        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[left])
                left += 1
            hashSet.add(s[r])
            res = max(res,r - left + 1) 
        return res         


        