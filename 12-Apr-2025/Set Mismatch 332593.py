# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        ans = []
        while i < n:
            correct_position = nums[i]-1
            if nums[i] != nums[correct_position]:
                nums[correct_position], nums[i] = nums[i], nums[correct_position]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i+1:      
                return [nums[i], i+1]
                                                                                                                                                          
        