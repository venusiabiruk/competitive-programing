# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x^y
        res = bin(temp)
        return res.count('1')
        

        