'''
Coderbyte: Tree Constructor
Solution by James Errington, 2024

Have the function TreeConstructor(strArr) take the array of strings stored in strArr, which will contain pairs of integers in the following format:
(i1,i2), where i1 represents a child node in a tree and the second integer i2 signifies that it is the parent of i1.
For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], then this forms the following tree:
which you can see forms a proper binary tree.
Your program should, in this case, return the string true because a valid binary tree can be formed.
If a proper binary tree cannot be formed with the integer pairs, then return the string false.
All of the integers within the tree will be unique, which means there can only be one node in the tree with the given integer value.
'''

from typing import List

def TreeConstructor(strArr: List[str]) -> str:
    nodes = set()
    parents = {}
    children = {}
    for pair in strArr:
        lstr, rstr = pair.split(",")
        c, p = int(lstr[1:]), int(rstr[:-1])
        nodes.add(c); nodes.add(p)
        if p in children:
            children[p] = children[p] + 1
        else:
            children[p] = 1

        if c in parents:
            parents[c] = parents[c] + 1
        else:
            parents[c] = 1

    if len(parents.values()) != len(nodes) - 1:
        return "false"
    for v in parents.values():
        if v != 1:
            return "false"
    for v in children.values():
        if v > 2:
            return "false"

    return "true"

print(TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]) == "true")
print(TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"]) == "false")
print(TreeConstructor(["(1,2)", "(2,4)", "(7,2)"]) == "true")
