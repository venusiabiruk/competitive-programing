# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = []
        d = {}
        for i in range(len(s)):
            d[indices[i]] = s[i]
        for j in range (len(s)):
            result.append(d[j])
       
        return "".join(result)