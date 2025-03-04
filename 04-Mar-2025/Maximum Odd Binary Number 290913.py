# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c_1 = s.count("1")
        c_0 = len(s) - c_1
        ans = []
        for i in range((c_1-1)):
            ans.append("1")
        for j in range(c_0):
            ans.append("0")
        ans.append("1")
        return("".join(ans))