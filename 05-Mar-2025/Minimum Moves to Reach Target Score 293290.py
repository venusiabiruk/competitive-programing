# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        max_double = maxDoubles
        min_step = 0
        if target == 1:
            return 0
        if maxDoubles == 0:
            return target-1
        while max_double > 0 and target != 1:
            if target%2 !=0:
                min_step +=2
                target = target//2
                max_double -=1
            else:
                min_step +=1
                target = target//2
                max_double -=1
        
        if  target != 1:
            min_step += target -1
        return min_step



        



        
        