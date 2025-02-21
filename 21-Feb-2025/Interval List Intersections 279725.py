# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        events = []
        for s, e in firstList:
            events.append((s, 1))
            events.append((e + 1, -1))
        for s, e in secondList:
            events.append((s, 1))
            events.append((e + 1, -1))
        events.sort()
        
        result = []
        count = 0
        prev = None
        for pos, delta in events:
            if prev is not None and count == 2:
                result.append([prev, pos - 1])
            count += delta
            prev = pos
        return result

        
        