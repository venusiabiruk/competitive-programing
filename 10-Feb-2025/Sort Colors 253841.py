# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i+1,(len(nums))):
                if nums[i] > nums[j]:
                    nums[i] ,nums[j] = nums[j] ,nums[i]
                else:
                    continue
        return nums








        # l,r = 0,len(nums)-1
        # while l <=r:
        #     if nums[l] > nums[r]:
        #         nums[l] , nums[r] = nums[r] , nums[l]
        #     else:
        #         r -= 1
        

        