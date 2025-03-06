# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_li = []
        t_li = []
        for i in s:
            if i != "#":
                s_li.append(i)
            else:
                if s_li:
                    s_li.pop()
        for j in t:
            if j != "#":
                t_li.append(j)
            else:
                if t_li:
                    t_li.pop()
        return s_li == t_li

            
        