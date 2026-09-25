class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap ={}
        l,res=0,0
        maxC = 0
        for r in range(len(s)):
            hashMap[s[r]] = 1 + hashMap.get(s[r],0)
            maxC = max(hashMap[s[r]],maxC)

            while (r-l+1) - maxC > k:
                hashMap[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res

        
        

        