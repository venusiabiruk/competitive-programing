# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        def helper(left, right):
        
            if left >= right:
                return
            s[right], s[left] = s[left], s[right]
            
            helper(left+1, right-1)
        helper(left, right)

        