class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0 
        l,r = 0, len(height)
        while(l<r):
            nextL = l+1 
            nextR = r-1
            if(nextL < l):
                while(nextL < l):
                    res += nexL-l
                    nextL += 1
            else:
                l +=1
            if nextR < r:
                while(nextR < r):
                    res+= r - nextR
                    nextR+=1
            else:
                r -= 1
        return res-1
        