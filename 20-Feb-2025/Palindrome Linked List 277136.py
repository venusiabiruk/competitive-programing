# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        compare = []
        cur = head
        while cur:
            compare.append(cur.val)
            cur = cur.next
        l,r = 0 ,len(compare)-1
        while l < r:
            if compare[l] != compare[r]:
                return False
            l+=1
            r-=1
        return True
       
    