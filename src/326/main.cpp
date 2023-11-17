/*
 * Leetcode Problem 326: Power of Three
 * Solution by James Errington, 2023
 *
 * Given an integer n, return true if it is a power of three. Otherwise, return false.
 * An integer n is a power of three, if there exists an integer x such that n == 3^x.
*/

#include "../shared.hpp"

class Solution {
public:
    static bool isPowerOfThree(int n) {
        return n > 0 && 1162261467 % n == 0;
    }
};

int main() {
    int tests[6] = {27, 0, -1, 9, 15, 1};

    for (auto x : tests) {
        auto result = Solution::isPowerOfThree(x);
        std::cout << x << " => " << result << std::endl;
    }
}
