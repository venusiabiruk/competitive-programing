# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
         
        half_rounds = time// (n-1)
        ans = 0
        if (half_rounds%2 == 0):
            ans = (1+time%(n-1))
        else:
            ans = (n-time%(n-1))
        return ans
        