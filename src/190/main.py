#
# Leetcode Problem 190: Reverse Bits
# Solution by James Errington, 2024
#
# Reverse bits of a given 32 bits unsigned integer.
#

class Solution:
    def reverseBits(self, n: int) -> int:
        return int("{:032b}".format(n)[::-1], 2)

tests = [
    "00000010100101000001111010011100",
    "11111111111111111111111111111101",

]

s = Solution()
for test in tests:
    res = s.reverseBits(int(test, 2))
    print(res)
