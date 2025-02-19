# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        cur = head 
        temp = head.next
        n = temp.next
        cur.next = None
        while n!= None:
            temp.next = cur
            cur = temp
            temp = n
            n = n.next
        temp.next = cur
        return temp 
        

            
        