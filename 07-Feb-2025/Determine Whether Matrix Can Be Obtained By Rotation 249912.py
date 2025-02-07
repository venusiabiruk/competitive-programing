# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True

        n = len(mat)

        for rotate in range(3):
            temp = [[0] * n for _ in range(n)]
            for rows in range(n):
                for columns in range(n):
                    temp[columns][n - 1 - rows] = mat[rows][columns]
            mat = temp
            if mat == target:
                return True 

        return False
     
