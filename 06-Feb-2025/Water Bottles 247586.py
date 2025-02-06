# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles
        while empty >= numExchange:
            drinkable = empty // numExchange
            total += drinkable
            extra = empty % numExchange
            empty = drinkable + extra
        return total




        