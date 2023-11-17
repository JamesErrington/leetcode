/*
 * Leetcode Problem 13: Roman to Integer
 * Solution by James Errington, 2023
 *
 * Given a roman numeral, convert it to an integer.
 * I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
 *
 * I before V or X
 * X before L or C
 * C before D or M
*/

#include "../shared.hpp"

class Solution {
public:
    static int romanToInt(std::string s) {
        int output = 0;

        for (auto iter = s.cbegin(); iter != s.cend(); iter++) {
            int increment = 0;
            switch (*iter) {
                case 'I': {
                    iter++;
                    switch (*iter) {
                        case 'V':
                            increment = 4; break;
                        case 'X':
                            increment = 9; break;
                        default: {
                            increment = 1;
                            iter--;
                        } break;
                    }
                } break;
                case 'V': {
                    increment = 5;
                } break;
                case 'X': {
                    iter++;
                    switch (*iter) {
                        case 'L':
                            increment = 40; break;
                        case 'C':
                            increment = 90; break;
                        default: {
                            increment = 10;
                            iter--;
                        } break;
                    }
                } break;
                case 'L': {
                    increment = 50;
                } break;
                case 'C': {
                    iter++;
                    switch (*iter) {
                        case 'D':
                            increment = 400; break;
                        case 'M':
                            increment = 900; break;
                        default: {
                            increment = 100;
                            iter--;
                        } break;
                    }
                } break;
                case 'D': {
                    increment = 500; break;
                } break;
                case 'M': {
                    increment = 1000; break;
                } break;
            }
            output += increment;
        }

        return output;
    }
};

int main() {
    std::string tests[4] = {
        "III",     // 1 + 1 + 1 = 3
        "LVIII",   // 50 + 5 + 1 + 1 + 1 = 58
        "MCMXCIV", // 1000 + (1000 - 100) + (100 - 10) + (5 - 1) = 1994
        "CDXLI",   // (500 - 100) + (50 - 10) + 1 = 441
    };

    for (auto x : tests) {
        auto result = Solution::romanToInt(x);
        std::cout << x << " = " << result << std::endl;
    }
}
