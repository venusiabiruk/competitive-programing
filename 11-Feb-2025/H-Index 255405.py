# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        max_num = 0
        for num in citations:
            if num <= n:
                max_num = max(max_num,num)
                n -=1
            else:
                max_num = max(max_num,n)
                
        return max_num
        