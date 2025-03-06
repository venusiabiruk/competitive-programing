# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures 
        n = len(t)
        a = [0] *n
        s = []
        for i ,t in enumerate(t):
            while s and s[-1][0] < t:
                st,si = s.pop()
                a[si] = i-si
            s.append((t,i))
        return a

                
        
        


        