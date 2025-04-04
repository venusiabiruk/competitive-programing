# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        ans = []
        while i < n:
            correct_position = nums[i] - 1
            if correct_position != i and nums[i] != nums[correct_position]:
                nums[correct_position], nums[i] = nums[i], nums[correct_position]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans



        