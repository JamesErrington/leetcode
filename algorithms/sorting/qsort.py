'''
Quicksort Practice
James Errington, 2024
'''

from typing import List

def sort(A: List[int]):
    qsort(A, 0, len(A) - 1)


def qsort(A: List[int], lo: int, hi: int):
    # Base case of recursion
    if lo < 0 or hi < lo:
        return
    # Find the point where the pivot is sorted
    p = partition(A, lo, hi)
    # Recursively sort the left side of the pivot
    qsort(A, lo, p - 1)
    # Recursively sort the right side of the pivot
    qsort(A, p + 1, hi)


def partition(A: List[int], lo: int, hi: int) -> int:
    # Pick a pivot, here the high pointer
    pivot = A[hi]
    # Initialise the left pivot index
    i = lo - 1
    # Loop over every element in the range
    for j in range(lo, hi):
        # If the element is less than the pivot
        if A[j] < pivot:
            # Move the left pivot index up one
            i += 1
            # Swap the current and the left pivot elements
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
    # The left pivot is now on the largest element < the pivot
    # Increment the left pivot one and swap in the pivot
    i += 1
    temp = A[i]
    A[i] = A[hi]
    A[hi] = temp
    return i


xs = [1,2,3,4,5]
sort(xs)
assert(xs == [1,2,3,4,5])

xs = [5,4,3,2,1]
sort(xs)
assert(xs == [1,2,3,4,5])

xs = [2,5,1,4,3]
sort(xs)
assert(xs == [1,2,3,4,5])

print("All tests passed!")
