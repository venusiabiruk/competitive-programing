# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l ,r = 0, len(s)-1
        while l <=r:
            if s[l] != s[r]:
                return s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]
            l+=1
            r-=1
        return True 

        