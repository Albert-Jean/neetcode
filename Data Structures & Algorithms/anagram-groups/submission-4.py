class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for s in strs:
            my_key = [0]*26
            for c in s:
                my_key[ord(c)-ord('a')] += 1 
            my_key = tuple(my_key)
            hashMap[my_key].append(s)
        return list(hashMap.values())