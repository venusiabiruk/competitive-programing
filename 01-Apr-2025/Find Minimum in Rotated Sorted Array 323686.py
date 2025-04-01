# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        cur_min = float("inf")
        while left <= right:
            mid = (left+right)//2
            if nums[left] <= nums[mid]:
                cur_min = min(cur_min,nums[left])
                left = mid +1
            else:
                cur_min = min(cur_min,nums[mid])
                right = mid -1
        return cur_min
       
        