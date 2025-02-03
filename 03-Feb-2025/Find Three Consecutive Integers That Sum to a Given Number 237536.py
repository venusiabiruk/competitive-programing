# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        num1 = math. floor(num/3)
        if (num1-1) + num1  +(num1+1) == num:
            return [(num1-1), num1, (num1+1)]
        else:
            return []
        