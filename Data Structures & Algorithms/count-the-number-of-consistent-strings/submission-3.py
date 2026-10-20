class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedMap = {}
        for c in allowed:
            allowedMap[c]= allowedMap.get(c,0)+1
        res=0
        for word in words:
            flag = True
            for c in word:
                if c not in allowedMap:   
                    flag = False                 
            if flag:
                res+=1        
        return res