# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            i = 0
            while i < (len(prefix)) and i < (len(s)) and prefix[i] == s[i]:
                i +=1
            prefix = prefix[:i]
        if not prefix:
            prefix = ""
        return prefix 
