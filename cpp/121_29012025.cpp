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
    int maxProfit(std::vector<int>& prices) {
        int i = 0;
        int min_1 =0, max_1=0, min_2=0, max_2 = 0;

        if (prices.size() < 2) {
            return 0;
        }

        while (i < prices.size()) {
            // initializing first min
            if (i == 0 or prices[i] < min_1 and min_1 != 0) {
                min_1 = prices[i];
            } 

            if ((min_1 != 0 and max_1 == 0 and prices[i] > min_1) or (max_1 != 0 and prices[i] > max_1)) {
                max_1 = prices[i];
            }
            i++;
        }
    if (max_1 - min_1 > 0) {
        return max_1 - min_1;
    } else {
        return 0;
    }        
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
