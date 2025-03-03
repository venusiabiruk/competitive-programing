# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        s = 0
        nums.sort(reverse = True)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                s = nums[i] + nums[i+1] + nums[i+2]
                return s
           
        return 0



        