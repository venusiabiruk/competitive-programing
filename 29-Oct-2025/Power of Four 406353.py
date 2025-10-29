# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def ispfour(n):
            if n == 1:
                return True
            elif n < 1:
                return False 
            else:
                return ispfour(n / 4)

        return ispfour(n)
