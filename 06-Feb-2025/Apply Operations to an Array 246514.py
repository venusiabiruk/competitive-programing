# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = []*n
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                continue
            else:
                nums[i] = nums[i]*2
                nums[i+1] =0
        for i in nums:
            if i != 0:
                l.append(i)
       
        for i in nums:
            if i == 0:
                l.append(i)
        return l




        