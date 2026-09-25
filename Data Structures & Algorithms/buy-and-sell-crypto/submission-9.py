class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, profit,maxProfit = 0,0,0
        n = len(prices)
        R=1
        while(R in range(1,n,1)):
            profit = prices[R] - prices[left]
            maxProfit = max(profit,maxProfit)
            if profit < 0:
                left +=1
                R = left + 1
            else: 
                R+=1
        return maxProfit
            
                
        