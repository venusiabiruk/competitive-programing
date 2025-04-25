# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        odd = [0]* len(graph)
        def bfs(i):
            if odd[i] != 0:
                return True
            q = deque([i])
            odd[i] = -1
            while q:
                i = q.popleft()
                for n in graph[i]:
                    if odd[n] == odd[i]:
                        return False
                    elif odd[n] == 0:
                        q.append(n)
                        odd[n] = -1 * odd[i]
            return True
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True
            