# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i in "+-*/":
                b ,a = s.pop(), s.pop()
                if i ==  '+':
                    s.append(a+b)
                elif i == '-':
                    s.append(a-b)
                elif i == '*':
                    s.append(a*b)
                elif i == '/':
                    d = a/b
                    if d < 0:
                        s.append(ceil(d))
                    else:
                        s.append(floor(d)) 
            else:
                s.append(int(i))
        return s[0]
        




        