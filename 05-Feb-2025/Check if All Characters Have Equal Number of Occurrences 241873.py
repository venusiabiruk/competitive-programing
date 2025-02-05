# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = Counter(s)
        v1 = list(d.values())[0]
        for i in d.values():
            if v1 != i:
                return False
            
        return True



        