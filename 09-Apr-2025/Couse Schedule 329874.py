# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for course, pre in prerequisites:
            adj_list[pre].append(course)
           
        white = 1
        black = 3
        gray = 2
        color = {course:white for course in range(numCourses)}
        no_cycle = True
        def dfs(node):
            nonlocal no_cycle
            if not no_cycle:
                return
             
            color[node] = gray
            for n in adj_list[node]:
                if color[n] == white:
                    dfs(n)
                if color[n] == gray:
                    no_cycle = False
            color[node] = black

        for course in range(numCourses):
            if color[course] == white:
                dfs(course)
        return  no_cycle
'''
[[1,0]]
2
[[1,0],[0,1]]
5
[[1,4],[2,4],[3,1],[3,2]]
6
[[1,0],[1,2],[3,1],[2,3],[2,4],[4,5],[2,5]]
6
[[1,0],[1,2],[3,1],[3,2],[2,4],[4,5],[2,5]]
'''