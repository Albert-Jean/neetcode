class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        l=0
        sMap = {}

        tMap = {}
        for i in range(len(t)):
            tMap[t[i]] = 1 + tMap.get(t[i],0)            
        
        res=""
        have, need = 0, len(tMap)
        for r in range(len(s)):
            sMap[s[r]] = 1 + sMap.get(s[r],0)
            if s[r] in tMap and sMap[s[r]] == tMap[s[r]]:
                have += 1
            while have == need:
                current_window = s[l:r+1]
                if res == "" or len(current_window) < len(res):
                    res = current_window
                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
                
        return res
