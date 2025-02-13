# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        res = []
        n = len(skill)
        mid = n//2
        s = []
        p = 0
        if n//2 == 1:
            return skill[0]*skill[1]
        l,r = 0, len(skill)-1
        while l <= r:
            s.append(skill[l] +skill[r])
            l +=1
            r -=1
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                return -1
        l,r = 0, len(skill)-1
        while l <= r:
            p += skill[l]*skill[r]
            l +=1
            r -=1
        return p
        


        
            



        

        
        