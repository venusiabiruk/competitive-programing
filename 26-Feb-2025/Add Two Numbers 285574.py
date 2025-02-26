# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ansh = ListNode()
        ans = ansh
        s = carry = 0
        while l1 and l2:
            curl1 = l1.val
            curl2 = l2.val
            s = curl1+curl2+carry
            ans.next = ListNode()
            ans.next.val = s%10
            carry = s//10
            l1 = l1.next
            l2 = l2.next
            ans = ans.next
        while l1:
            curl1 = l1.val
            s = curl1+carry
            ans.next = ListNode()
            
            ans.next.val = s%10
            carry = s//10
            l1 = l1.next
            ans = ans.next
        while  l2:
            curl2 = l2.val
            s = curl2+carry
            ans.next = ListNode()
            
            ans.next.val = s%10
            carry = s//10
            l2 = l2.next
            ans = ans.next
        if carry != 0:
            ans.next = ListNode() 
            ans.next.val = carry
        return ansh.next




        

        