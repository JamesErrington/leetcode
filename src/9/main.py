'''
Leetcode Problem 9: Palindrome Number
Solution by James Errington, 2024

Given an integer x, return true if x is a palindrome, and false otherwise.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]

        if x < 0:
            return False

        digits = []
        while x > 0:
            r = x % 10
            digits.append(r)
            x = x // 10

        n = len(digits)
        for i in range(n // 2):
            if digits[i] != digits[n - i - 1]:
                return False
        return True



s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
