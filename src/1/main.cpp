/*
 * Leetcode Problem 1: Two Sum
 * Solution by James Errington, 2023
 *
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
*/

#include "../shared.hpp"
#include <unordered_map>

class Solution {
public:
    static std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> cache;

        for (unsigned int i = 0; i < nums.size(); i++) {
            auto value = nums[i];

            auto found = cache.find(target - value);
            if (found != cache.end()) {
                return std::vector<int>{cache[target - value], (int)i};
            } else {
                cache[value] = i;
            }
        }

        return std::vector<int>{};
    }
};

struct Test {
    std::vector<int> nums;
    int target;
};

int main() {
    Test tests[3] = {
        { std::vector{2, 7, 11, 15}, 9 }, // [0, 1] or [1, 0]
        { std::vector{3, 2, 4}, 6 },      // [1, 2] or [2, 1]
        { std::vector{3, 3}, 6 },         // [0, 1] or [1, 0]

    };

    for (auto test : tests) {
        auto result = Solution::twoSum(test.nums, test.target);
        std::cout << "[";
        for (auto x : result) {
            std::cout << " " << x << " ";
        }
        std::cout << "]" << std::endl;
    }
}
