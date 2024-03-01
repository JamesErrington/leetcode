#
# Leetcode Problem 28: Find the Index of the First Occurrence in a String
# Solution by James Errington, 2024
#
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


s = Solution()
print(s.strStr("sadbutsad", "sad"))
print(s.strStr("leetcode", "leeto"))
print(s.strStr("leetcode", "e"))
