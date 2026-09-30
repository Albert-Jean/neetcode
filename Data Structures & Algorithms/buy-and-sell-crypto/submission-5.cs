public class Solution {
    public int MaxProfit(int[] prices) {
       int buyDay=0;
       int sellDay=1;
       int maxP = 0;
       while(sellDay<prices.Length){
        if(prices[sellDay]>prices[buyDay]){
            maxP = prices[buyDay]-prices[sellDay];
        }
        else{
            buyDay=sellDay;
        }
        sellDay++;
       }
       return Math.Abs(maxP);
    }
}
