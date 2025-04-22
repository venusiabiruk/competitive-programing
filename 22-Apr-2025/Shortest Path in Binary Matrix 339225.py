# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque([(0,0,1)])
        visted = set((0,0))
        d = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        while q:
            r, c, l = q.popleft()
            if min(r,c) < 0 or max(r,c) >= n or grid[r][c]:
                continue
            if c == n-1 and r == n-1:
                return l
            for dr , dc in d:
                if (r+dr,c+dc) not in visted:
                    q.append((r+dr,c+dc,l+1))
                    visted.add((r+dr,c+dc))
        return -1 
            

        