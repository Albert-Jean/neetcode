class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, profit,maxProfit = 0,0,0
        n = len(prices)
        lenght = n+1

        for R in range(1,n,1):
            profit = prices[R] - prices[left]
            maxProfit = max(profit,maxProfit)
            if profit <= 0:
                left +=1
                R = left
        return int(maxProfit)
            
                
        