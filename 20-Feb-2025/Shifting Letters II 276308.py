# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        res = [ord(c) - ord("a") for c in s]
        prefix_dif = [0]*(len(s)+1)
        dif = 0
        for l,r,shift in shifts:
            if shift == 0:
                prefix_dif[r+1] -=1
                prefix_dif[l]+=1
            else:
                prefix_dif[r+1]+=1
                prefix_dif[l]-=1
        for i in range(len(prefix_dif) - 1, -1, -1):
            dif += prefix_dif[i]
            res[i-1] = (dif+res[i-1])%26
        s = [chr(ord("a")+n) for n in res]
        return "".join(s)



