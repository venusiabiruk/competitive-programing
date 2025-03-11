# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = Counter(answers)
        s = 0
        for key,val in ans.items():
            if key == 0:
                s += val
            else:
                groups = val//(key+1)
                s += groups*(key+1)
                r = val%(key+1)
                if r != 0:
                    s += (key+1)
        return s

        
       






        