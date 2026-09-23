class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r
        while l <= r:
            speed = (l + r)//2
            if  self.getEatingTime(piles,speed) > h :
                l = speed + 1
            else:
                res = speed
                r = speed - 1
        return res


    def getEatingTime(self,piles: List[int], speed: int) -> int:
        time = 0
        for pile in piles:
            time += math.ceil(pile / speed)
        return time
