# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        res = [[-1 for _ in range(n)] for _ in range(m)]
        q = deque()
        for r in range(m):
            for c in range(n):
                if isWater[r][c] == 1:
                    res[r][c] = 0
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            for dr , dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and res[nr][nc] == -1:
                    res[nr][nc] = res[r][c] + 1
                    q.append((nr, nc))
        
        return res