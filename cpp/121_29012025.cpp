/*
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
*/
#include <iostream>
#include <vector>

class Solution {
    public:
        int maxProfit(std::vector<int> & prices) {
            int maxProfit = 0, min = 0, max = 0;
            int i;
            if (prices.size() < 2) {
                return 0;
            }

            while (i < prices.size()) {
                // min case
                if (i == 0 or prices[i] < min) {
                    min = prices[i];
                }
                // max case
                else if (max < prices[i]) {
                        max = prices[i];
                    }
                

                if (max - min >= maxProfit) {
                    maxProfit = max - min;
                    // max = 0;
                }
                max = 0;
                i++;

            }
            return maxProfit;
        }    
};


int main() {
    Solution solution;
    std::vector<int> prices;// = {1, 3, 5};
    prices.push_back(1);
    prices.push_back(3);
    prices.push_back(5);
    solution.maxProfit(prices);

}
