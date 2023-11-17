/*
 * Leetcode Problem 1877: Minimize Maximum Pair Sum in Array
 * Solution by James Errington, 2023
 *
 * The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.
 * Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:
 * - Each element of nums is in exactly one pair, and
 * - The maximum pair sum is minimized.
 * Return the minimized maximum pair sum after optimally pairing up the elements.
*/

#include "../shared.hpp"

class Solution {
public:
    static int minPairSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());

        int maximum = 0;
        auto size = nums.size();
        for (int i = 0; i < size / 2; i++) {
            maximum = std::max(maximum, nums[i] + nums[size - 1 - i]);
        }

        return maximum;
    }
};

int main() {
    std::vector<int> tests[5] = {
        std::vector<int>{ 3, 5, 2, 3 },
        std::vector<int>{ 3, 5, 4, 2, 4, 6 },
        std::vector<int>{ 3, 5 },
        std::vector<int>{ 1, 2, 3, 4, 5, 6 },
        std::vector<int>{ 20, 15, 3, 7, 10, 9, 4, 2 },
    };

    for (auto x : tests) {
        auto result = Solution::minPairSum(x);
        std::cout << result << std::endl;
    }
};
