# Problem: Fizz Buzz - https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l =[]
        for i in range(n,0,-1):
            if i%3 == 0 and i%5 == 0:
                l.append("FizzBuzz")
            elif i%3==0 and i%5 != 0:
                l.append("Fizz")
            elif i%5 == 0 and i%3 != 0:
                l.append("Buzz")
            else:
                l.append(str(i))
        l.reverse()
        return l


        