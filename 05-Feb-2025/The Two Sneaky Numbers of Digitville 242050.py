# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        l = []
        for i in d:
            if d[i] > 1:
                l.append(i)
        return l