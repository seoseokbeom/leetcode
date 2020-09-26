# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        node = head
        while node:
            curr = node
            node = node.next
            curr.next = prev
            prev = curr
        return prev
