# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())

        def helper(l, r):
            if l >= r:
                return True
            if s[l] != s[r]:
                return False
            return helper(l+1,r-1)
        return helper(0,len(s)-1)

