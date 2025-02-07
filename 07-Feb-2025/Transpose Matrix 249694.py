# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        col_len = len(matrix[0])
        row_len = len(matrix)
        temp = [[0]*row_len for i in range(col_len)]
        for row in range (row_len):
            for col in range(col_len):
                temp[col][row] = matrix[row][col] 
        return temp


       