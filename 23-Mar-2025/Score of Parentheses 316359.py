# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        OP = False
        S = []
        count = 0
        for score in s:
            if score == "(":
                OP = True
                S.append(score)
            else:
                if OP:
                    count += 2**(len(S)-1)
                    OP = False
                S.pop()
        return count
        