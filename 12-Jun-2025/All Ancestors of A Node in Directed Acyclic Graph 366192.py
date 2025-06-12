# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
        visited = [False] * n
        order = []
        def dfs(u):
            visited[u] = True
            for w in g[u]:
                if not visited[w]:
                    dfs(w)
            order.append(u)
        for i in range(n):
            if not visited[i]:
                dfs(i)
        order.reverse()
        rg = defaultdict(list)
        for u, v in edges:
            rg[v].append(u)
            
        anc = [set() for _ in range(n)]
        
        for u in order:
            for p in rg[u]:
                anc[u].add(p)
                anc[u].update(anc[p])
        
        return [sorted(list(s)) for s in anc]
        

        