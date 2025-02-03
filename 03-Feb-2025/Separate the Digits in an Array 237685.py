# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l = ( "".join(map(str,nums)))
        return[ int(i) for i in l]

        