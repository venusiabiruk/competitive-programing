# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        l = []
        d = Counter(s)
        arranged = sorted(d.items(), key = lambda x:x[1],reverse=True)
        for key,v in arranged:
            l.append(key*v) 
        return "".join(l)