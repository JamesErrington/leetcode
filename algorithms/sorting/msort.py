'''
Mergesort Practice
James Errington, 2024
'''

from typing import List

def sort(A: List[int]) -> List[int]:
    return msort(A)


def msort(A: List[int]) -> List[int]:
    # Base case of the recursion
    if len(A) == 1:
        return A
    # Recursively sort the left sublist
    left = msort(A[0:len(A)//2])
    # Recursively sort the right sublist
    right = msort(A[len(A)//2:len(A)])
    # Merge the two sublists
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    # The sorted output list
    result = []
    # Loop through every comparison
    while left and right:
        # Append the least element in the comparison to the output and pop it from the sublist
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # Either the left or right will have elements left, so we append these here
    result += left
    result += right
    return result


xs = [1,2,3,4,5]
ys = sort(xs)
assert(ys == [1,2,3,4,5])

xs = [5,4,3,2,1]
ys = sort(xs)
assert(ys == [1,2,3,4,5])

xs = [2,5,1,4,3]
ys = sort(xs)
assert(ys == [1,2,3,4,5])

print("All tests passed!")
