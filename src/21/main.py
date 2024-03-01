#
# Leetcode Problem 21: Merge Two Sorted Lists
# Solution by James Errington, 2024
#
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
#

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        ptr1 = list1
        ptr2 = list2

        while True:
            if ptr1 is None:
                tail.next = ptr2; break
            elif ptr2 is None:
                tail.next = ptr1; break

            if ptr1.val <= ptr2.val:
                tail.next = ptr1
                ptr1 = ptr1.next
            else:
                tail.next = ptr2
                ptr2 = ptr2.next

            tail = tail.next

        return head.next
