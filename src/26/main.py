#
# Leetcode Problem 26: Remove Duplicates from Sorted Array
# Solution by James Errington, 2024
#
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.
#

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        markers = []

        i = 0
        while i < len(nums):
            curr = nums[i]
            while i + 1 < len(nums) and nums[i + 1] == curr:
                i += 1
            markers.append(i)
            i += 1

        for i in range(1, len(markers)):
            nums[i] = nums[markers[i - 1] + 1]
        return len(markers)

tests = [
    [0,0,1,1,1,2,2,3,3,4],
    [],
    [1,1,2],
    [-1, -1, -1, 0, 0, 1, 2, 3, 3, 5, 7, 7, 8, 9, 9]
]

s = Solution()
for test in tests:
    res = s.removeDuplicates(test)
    print(res, test)
