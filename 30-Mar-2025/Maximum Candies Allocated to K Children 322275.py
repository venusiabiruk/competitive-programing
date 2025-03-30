# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 0, max(candies)
        def is_valid(mid):
            count = 0
            for i in candies:
                count += i // mid
            return count >= k
        while left < right:
            mid = (left + right + 1) // 2
            if is_valid(mid):
                left = mid
            else:
                right = mid - 1  
        return left