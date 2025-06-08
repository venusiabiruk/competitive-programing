# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m , n = len(board), len(board[0])
        direction = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[1,1],[1,-1],[-1,1]]
        q = deque()
        q.append((click[0], click[1]))
        while q:
            r, c = q.popleft()
            
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return board
            
            mines = 0
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    mines += 1
            if mines == 0:
                board[r][c] = 'B'
                for dr, dc in direction:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'E':
                        board[nr][nc] = 'B'
                        q.append((nr, nc))
            else:
                board[r][c] = str(mines)
        
        return board
        



        