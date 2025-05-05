# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[-1 for _ in range(n)] for _ in range(m)]
        q = deque()
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    res[r][c] = 0
                    q.append((r,c))
        while q:
            r,c  = q.popleft()
            for dc, dr in direction:
                nr= r+dr
                nc = c+dc
                if 0 <= nr < m and 0 <= nc < n and res[nr][nc] == -1:
                    res[nr][nc] = res[r][c]+1
                    q.append((nr, nc))
        return res

        
        