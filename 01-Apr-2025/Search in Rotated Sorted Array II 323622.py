# Problem: Search in Rotated Sorted Array II - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] and nums[right] == nums[mid]:
                left +=1
                right -=1
                continue
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid -1
                else:
                    left = mid +1
            else:
                if target <= nums[right] and target >=nums[mid]:
                    left = mid+1
                else:
                    right = mid -1
        return False
        