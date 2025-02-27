# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head 
        odd = head
        o = odd
        even = head.next
        e = even
        while  e and e.next:
            o.next = o.next.next
            o = o.next
            e.next = o.next
            e = e.next
        o.next = even
        return odd

      





        