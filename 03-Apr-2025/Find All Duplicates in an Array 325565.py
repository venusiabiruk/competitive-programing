# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            idx = abs(i)
            if nums[idx-1] > 0:
                nums[idx-1] = -nums[idx-1]
            else:
                ans.append(idx)
        return ans 

        