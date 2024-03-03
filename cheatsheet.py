# Format a number as binary
format(12, "b") # 1100
# Format with leading 0s
format(12, "06b") # 001100
n = 5
format(12, f"0{n}b") # 01100

xs = [1,2]
for index, value in enumerate(xs):
    continue

# String methods
", ".join(["a", "b", "c"]) # a, b, c
"some text here".title() # Some Text Here
"hello mum".count("l") # 2
"hello mum".find("mum") # 6
"hello mum".find("foo") # -1
"hello mum".replace("hello", "hi") # "hi mum"
"HelLo mUm".swapcase() # "hELlO MuM"

# Reverse
xs = [1,2,3]
xs[::-1] # [3,2,1]

# Reverse bits of binary number
# int("{:032b}".format(n)[::-1], 2)

# In place assignment
xs[:] = sorted(xs) # [1,2,3]

# Sort on key
xs = [(1, 0), (0, 1)]
sorted(xs, key=lambda x: x[0]) # [(0, 1), (1, 0)]

def isPalindrome(s: str):
    return str(s) == str(s)[::-1]

'''
Remove duplicates in place
nums[:] = sorted(set(nums))

Or

j = 0
for i in range(1, len(nums)):
	if nums[j] != nums[i]:
		j += 1
		nums[j] = nums[i]
return j + 1
'''

'''
Iterate a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while curr:
            stack.append(curr)
            curr = curr.left

        it = 1
        while it < k and len(stack) > 0:
            curr = stack[-1].right
            stack.pop()
            while curr:
                stack.append(curr)
                curr = curr.left
            if it == k:
                return stack[-1].val
            it += 1
        return stack[-1].val
'''

'''
Invert a binary tree
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.right, root.left = root.left, root.right

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
'''
