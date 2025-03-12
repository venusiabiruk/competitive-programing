# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            prev = self.getRow(rowIndex-1)
        cur = [1]
        for i in range(1,rowIndex):
            cur.append(prev[i-1]+prev[i])

        cur.append(1)
        return cur
        

        


        