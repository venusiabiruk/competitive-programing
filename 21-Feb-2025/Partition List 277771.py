# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left,right = ListNode(),ListNode()
        leftt , rightt = left, right
        while head:
            if head.val < x:
                leftt.next = head
                leftt = leftt.next
            else:
                rightt.next = head
                rightt = rightt.next
            head = head.next
        leftt.next = right.next
        rightt.next = None
        return left.next


        