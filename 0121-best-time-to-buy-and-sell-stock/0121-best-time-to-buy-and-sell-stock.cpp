class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int minbuy = prices[0];
        for(int i=1;i<prices.size();i++){

            int price = prices[i];
            profit = max(profit, price - minbuy);
            minbuy = min (minbuy, price);
        }
        return profit;
        
    }
};