# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans_left = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r+l)//2
            if nums[mid] == target:
                ans_left = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        ans_right = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r+l)//2
            if nums[mid] == target:
                ans_right = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return [ans_left, ans_right]
