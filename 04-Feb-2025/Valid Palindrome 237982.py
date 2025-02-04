# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        li =[]
    
        
        for i in range(len(s)):
            if  s[i].isalnum():
                li.append(s[i].lower())
        l,r = 0 ,(len(li)-1)
        while l<=r:
            if li[l] != li[r]:
                return False
            l+=1
            r-=1

            
        return True

            

                
        
        