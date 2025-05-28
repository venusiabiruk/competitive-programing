# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)])
        res = []
        min_heap = []
        time = 0
        i = 0
        n = len(tasks)
        while i < n or min_heap:
            while i < n and indexed_tasks[i][0] <= time:
                heappush(min_heap, (indexed_tasks[i][1], indexed_tasks[i][2]))
                i += 1
            if min_heap:
                proc_time, idx = heappop(min_heap)
                time += proc_time
                res.append(idx)
            else:
                time = indexed_tasks[i][0]
        return res
        