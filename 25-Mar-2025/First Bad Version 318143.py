# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        bad_left = 0
        l,r = 1, n
        while l <= r:
            mid = (r+l)//2
            if isBadVersion(mid):
                bad_left = mid
                r = mid -1
            else:
                l = mid +1 
        return bad_left
        