# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        q = deque()
        q.append((sr,sc))
        start =  image[sr][sc]
        image[sr][sc] = color
        if start == color:
            return image
        while q:
            r, c = q.popleft()
            for dc, dr in direction:
                nr, nc = r+dr, c+dc
                if nr >=0 and nr < m and nc >= 0 and nc < n and start== image[nr][nc]:
                    image[nr][nc] = color
                    q.append((nr,nc))
        
        return image


               
                 

        