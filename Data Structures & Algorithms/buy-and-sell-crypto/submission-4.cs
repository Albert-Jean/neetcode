public class Solution {
    public int MaxProfit(int[] prices) {
       Dictionary<int,int> map = new Dictionary<int,int>();
       int maxSell=1;
       int minBuy=prices[0];
       for(int i=1;i<prices.Count()-1;i++){
            if(prices[i]<prices[i+1]){               
                if(prices[i]< minBuy){
                    minBuy=prices[i];
                }
            }
            if(prices[i]>prices[i-1]){
                if(prices[i]> maxSell){
                    maxSell=prices[i];
                }
            }
       }
        Console.WriteLine("MinBuy:"+minBuy+" MaxSell:"+maxSell);
       if(maxSell<prices[prices.Count()-1]){
        maxSell=prices[prices.Count()-1];
       }
       if(maxSell-minBuy<=0){
        return 0;
       }      
       return maxSell-minBuy;
    }
}
