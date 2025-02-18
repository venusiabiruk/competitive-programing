# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        string_last_occ = {}
        for i in range(len(s)-1,-1,-1):
            if s[i] not in string_last_occ:
                string_last_occ[s[i]] = i
        r = 0
        l = 0
        for i in range(len(s)):
            r = max(r,string_last_occ[s[i]])
            if i == r:
                res.append(r - l + 1)
                l = i + 1
        return res
                



            

        











        