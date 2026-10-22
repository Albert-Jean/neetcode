class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return[newInterval]
        n = len(intervals)
        target = newInterval[0]
        l,r = 0, n-1
        #binary search to find where to add newInterval
        while l <= r:
            m = (l+r)//2
            if intervals[m][0]<target:
                l=m+1
            else:
                r=m-1
        #add new interval at left index
        intervals.insert(l,newInterval)
        #combine intervals if possible
        res=[]
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1],interval[1])
        return res
        