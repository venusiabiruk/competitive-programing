# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      
        d = Counter(nums)
        sorted_d = sorted(d.keys(), key=lambda x: d[x], reverse=True)
        return sorted_d[:k]