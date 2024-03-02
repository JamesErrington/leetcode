'''
Leetcode Problem 75: Sort Colors
Solution by James Errington, 2024

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
'''

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        qsort(nums, 0, len(nums) - 1)
        print(nums)


def qsort(A: List[int], lo: int, hi: int):
    if lo >= hi or lo < 0:
        return

    p = partition(A, lo, hi)
    qsort(A, lo, p - 1)
    qsort(A, p + 1, hi)

def partition(A: List[int], lo: int, hi: int):
    pivot = A[hi]
    i = lo - 1

    for j in range(lo, hi):
        if A[j] < pivot:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    i += 1
    temp = A[i]
    A[i] = A[hi]
    A[hi] = temp
    return i

s = Solution()
s.sortColors([3, 7, 8, 5, 2, 1, 9 , 5, 4])
s.sortColors([2,0,1])
