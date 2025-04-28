# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        for u ,v in redEdges:
            red[u].append(v)
        for u ,v in blueEdges:
            blue[u].append(v)
        ans = [-1 for i in range(n)]
        q = deque()
        q.append([0,0,None])
        visited = set()
        visited.add((0,None))
        while q:
            node, l , color = q.popleft()
            if ans[node] == -1:
                ans[node] = l
            if color != "red":
                for n in red[node]:
                    if (n,"red") not in visited:
                        visited.add((n,"red"))
                        q.append([n,l+1,"red"])
            if color != "blue":
                for n in blue[node]:
                    if (n,"blue") not in visited:
                        visited.add((n,"blue"))
                        q.append((n,l+1,"blue"))
        return ans 



        
        
        
        
        