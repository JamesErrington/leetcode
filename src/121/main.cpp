/*
 * Leetcode Problem 121: Best Time to Buy and Sell Stock
 * Solution by James Errington, 2023
 *
 * You are given an array prices where prices[i] is the price of a given stock on the ith day.
 * You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
 * Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
*/

#include "../shared.hpp"

class Solution {
public:
    static int maxProfit(std::vector<int>& prices) {
        int max_profit = 0;
        int lowest_price = prices[0];

        for (auto x : prices) {
            lowest_price = std::min(x, lowest_price);
            max_profit = std::max(max_profit, x - lowest_price);
        }

        return max_profit;
    }
};

int main() {
    std::vector<int> tests[4] = {
        std::vector<int>{7, 1, 5, 3, 6, 4},
        std::vector<int>{7, 6, 4, 3, 2, 1},
        std::vector<int>{5, 2, 8, 10, 7, 4},
        std::vector<int>{1, 2, 3, 4, 5},

    };

    for (auto x : tests) {
        auto result = Solution::maxProfit(x);
        std::cout << "Max Profit: " << result << std::endl;
    }
}
