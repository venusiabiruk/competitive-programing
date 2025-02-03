# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num= []
        
        st= ""
        for i in s:
            i = ((ord(i) - ord('a') + 1))
            num.append((i))
            st = "".join(map(str,num))
        for _ in range(k):
            st = str(sum(int(digit) for digit in st))  

        return int(st)

        
    
        