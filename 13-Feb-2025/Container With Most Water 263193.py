# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ma = 0
        while l < r:
            h = min(height[l],height[r])
            w = r-l
            a = h*w
            ma = max(ma,a)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return ma
