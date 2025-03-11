# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        def factorial(num):
            if num == 1 or num == 0:
                return 1
            else:
                return num*factorial(num-1)
        number = (factorial(n))
        while number%10 == 0:
            count += 1
            number = number//10
        return count

        
        
        

    


        