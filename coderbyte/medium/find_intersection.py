'''
Solution by James Errington, 2024

Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements:
the first element will represent a list of comma-separated numbers sorted in ascending order,
the second element will represent a second list of comma-separated numbers (also sorted).
Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order.
If there is no intersection, return the string false.
'''

from typing import List

def FindIntersection(strArr: List[str]):
    xs = set(strArr[0].split(", ")).intersection(strArr[1].split(", "))
    if len(xs) == 0:
        return "false"
    return ", ".join([str(y) for y in sorted([int(x) for x in xs])])

print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))
print(FindIntersection(["1", "0"]))
