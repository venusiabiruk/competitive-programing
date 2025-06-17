# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)

        n = len(quiet)
        answer = [-1] * n

        def dfs(x):
            if answer[x] != -1:
                return answer[x]
            answer[x] = x
            for nei in graph[x]:
                cand = dfs(nei)
                if quiet[cand] < quiet[answer[x]]:
                    answer[x] = cand
            return answer[x]

        for i in range(n):
            dfs(i)

        return answer
        