'''
Leetcode Problem 830: Positions of Large Groups
Solution by James Errington, 2024

In a string s of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".
A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group.
In the above example, "xxxx" has the interval [3,6].
A group is considered large if it has 3 or more characters.
Return the intervals of every large group sorted in increasing order by start index.
'''

from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i = 0
        groups = []
        while i < len(s):
            letter = s[i]
            start = i
            end = i
            if i == len(s) - 1:
                if end - start > 1:
                    groups.append([start, end])
                break
            while i < len(s) - 1:
                i += 1
                if s[i] == letter:
                    end = i
                    continue
                else:
                    break
            if end - start > 1:
                groups.append([start, end])
        return sorted(groups, key=lambda x: x[0])


s = Solution()
# print(s.largeGroupPositions("abbxxxxzzy"))
print(s.largeGroupPositions("abcdddeeeeaabbbcd"))
# print(s.largeGroupPositions("abc"))
