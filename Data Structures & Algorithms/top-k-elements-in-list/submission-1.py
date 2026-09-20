class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # key: dup number  value: number of dup
        bucketSortArr = [[]for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for key,v in count.items():
            bucketSortArr[v].append(key)
        res = []
        for i in range(len(bucketSortArr)-1,0,-1):
            for n in bucketSortArr[i]:
                res.append(n)
                if len(res)==k:
                    return res


            

            

        