# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u ,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        num_complete = 0
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                q = deque([i])
                visited[i] = True
                nodes = set()
                edge_c = 0
                while q:
                    node = q.pop()
                    nodes.add(node)
                    for n in graph[node]:
                        edge_c +=1
                        if not visited[n]:
                            visited[n]=True
                            q.append(n)
                            
                count_node = len(nodes)
                count_edge = edge_c//2
                if count_edge == count_node * (count_node - 1) // 2:
                            num_complete += 1

        return num_complete
        
        



        
      