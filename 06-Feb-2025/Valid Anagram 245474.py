# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = Counter(s)
        td = Counter(t)
        return sd == td
    
        