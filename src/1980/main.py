'''
Leetcode Problem 1980: Find Unique Binary String
Solution by James Errington, 2024

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums.
If there are multiple answers, you may return any of them.
'''

from typing import List

'''
The naive python way:

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        v = set(nums)
        print(v)
        for i in range(n**2 + 1):
            b = format(i, f"0{n}b")
            print(b)
            if b not in v:
                return b
'''

'''
The cool way
'''
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join([str(1 - int(b[i])) for i, b in enumerate(nums)])


s = Solution()
print(s.findDifferentBinaryString(["01","10"]))
print(s.findDifferentBinaryString(["00","01"]))
print(s.findDifferentBinaryString(["111","011","001"]))
print(s.findDifferentBinaryString(["0"]))
