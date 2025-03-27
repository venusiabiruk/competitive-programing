# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_cap(capacity):
            summ = 0
            d = 0
            for weight in weights:
                if summ + weight> mid:
                    d +=1
                    summ = weight 
                else:
                    summ += weight
            return d+1 
        cap = 0   
        lo = max(weights)
        hi = sum(weights)
        while hi >=lo:
            mid = (hi +lo)//2
            if is_cap(mid) <= days:
                cap = mid
                hi = mid-1
            else:
                lo = mid + 1
        return cap 
            

        
                
            




        