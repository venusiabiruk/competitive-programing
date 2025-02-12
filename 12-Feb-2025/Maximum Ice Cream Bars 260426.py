# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        # [1,1,2,3,4,5]
        l = 0
        s = 0
        while l < len(costs):
            s += costs[l]
            if s > coins:
                break 
            else: 
                l +=1
        return l
            
        


        