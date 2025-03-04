# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total = 0
        c_l = 0
        c_r = 0
        for i in s:
            if i == "R":
                c_r +=1
            elif i == "L":
                c_l +=1
            if c_l == c_r:
                total +=1
                c_l = 0
                c_r = 0
        return total
           

        

        