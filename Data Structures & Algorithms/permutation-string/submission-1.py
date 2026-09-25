class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        #store the chat of s1 + counter in a hashmap
        for c in s1:
            s1Map[c] = 1 + s1Map.get(c,0)
        
        s2Map = {}
        l = 0
        for r in range(len(s2)):
            s2Map[s2[r]] = 1 + s2Map.get(s2[r], 0)
            
            if r - l + 1 > len(s1):
                s2Map[s2[l]] -= 1
                if s2Map[s2[l]] == 0:
                    del s2Map[s2[l]]
                l += 1
                
            if s1Map == s2Map:
                return True

        return False
        