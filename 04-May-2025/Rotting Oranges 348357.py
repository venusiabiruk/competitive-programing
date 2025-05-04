# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        q = deque()
        time = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
        direction = [[1,0], [-1,0],[0,-1],[0,1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    new_r , new_c = r+dr, c+dc
                    if (new_r < 0) or (new_r >= m) or (new_c < 0) or (new_c >= n) or grid[new_r][new_c]!= 1:
                        continue 
                    grid[new_r][new_c] =2
                    q.append([new_r ,new_c])
                    fresh -=1
            time +=1
        return time if fresh == 0 else -1
                    

    

        