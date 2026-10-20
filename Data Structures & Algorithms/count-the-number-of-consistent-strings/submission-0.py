class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedMap = {}
        for c in allowed:
            allowedMap[c]= allowedMap.get(c,0)+1
        res=0
        for word in words:
            for c in word:
                if c in allowedMap:                    
                    word  = word.replace(c,"")
                    print(word)
            if word == "":
                    res +=1   
        return res