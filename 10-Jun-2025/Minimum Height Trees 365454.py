# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        l = [i for i in range(n) if len(g[i]) == 1]
        r = n
        while r > 2:
            r -= len(l)
            nl = []
            for x in l:
                y = g[x].pop()
                g[y].remove(x)
                if len(g[y]) == 1:
                    nl.append(y)
            l = nl
        return l
        