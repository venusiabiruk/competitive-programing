# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(i):
            q = deque()
            q.append(i)
            visited.add(i)
            while q:
                cur = q.popleft()
                for n in range(len(isConnected)):
                    if isConnected[cur][n] == 1 and n not in visited:
                        q.append(n)
                        visited.add(n)
        visited = set()
        p = 0
        for i in range(len(isConnected)):
            if i not in visited:
                bfs(i)
                p += 1
        return p 
            


                    
        
               


        
        