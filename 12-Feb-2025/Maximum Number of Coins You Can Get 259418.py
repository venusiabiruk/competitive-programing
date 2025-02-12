# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # [1,2,3,4,5,6,7,8,9] [1,8,9] [2,6,7] [3,4,5]
        piles.sort()
        n = len(piles)
        r = n//3
        s = 0
        for i in range(n-2,r-2,-2):
            s += piles[i]
        return s



                

            