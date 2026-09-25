class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for n in nums:
            hashMap[n] = 1 + hashMap.get(n,0)
        freq = [[] for _ in range(len(nums) + 1)]
        for num, c in hashMap.items():
            freq[c].append(num)
        res = []
        for c in range(len(freq) - 1, 0, -1):   # from highest freq to 1
            for num in freq[c]:
                res.append(num)
                if len(res) == k:
                    return res       
        return []