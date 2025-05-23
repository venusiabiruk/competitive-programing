# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        max_heap = []
        for idx , row in enumerate(grid):
            sort_row = sorted(row, reverse=True)
            for i in sort_row[:limits[idx]]:
                heapq.heappush(max_heap, -i)     
        total = 0
        for _ in range(min(k, len(max_heap))):
            total += -heapq.heappop(max_heap) 
        return total

        