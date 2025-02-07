# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        ans = []
        maximum_len = 0
        for i in s:
            maximum_len = max(len(i),maximum_len)
        for i in range(maximum_len):
            word = []
            for j in range(len(s)):
                if i >= (len(s[j])):
                    word.append(" ")
                else:
                    word.append(s[j][i])
            ans.append(("".join(word)).rstrip())
        return ans

            
        
        