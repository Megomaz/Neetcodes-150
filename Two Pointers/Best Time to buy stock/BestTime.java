class Solution {
    public int maxProfit(int[] prices) {
        int price = 0;
        int min = Integer.MAX_VALUE;
        int max = 0;
        int bestprice = 0;

        for (int num: prices){
            max = Math.max(max,num);
            if (num < min){
                min = num;
                max = 0;
            }
            bestprice = Math.max(bestprice,max - min);
        }

        return bestprice;
    }
}
/* 2 pointer solution
public class Solution {
    public int maxProfit(int[] prices) {
        int l = 0, r = 1;
        int maxP = 0;

        while (r < prices.length) {
            if (prices[l] < prices[r]) {
                int profit = prices[r] - prices[l];
                maxP = Math.max(maxP, profit);
            } else {
                l = r;
            }
            r++;
        }
        return maxP;
    }
}
*/