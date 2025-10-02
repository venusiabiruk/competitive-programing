# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        rob1, rob2 =  0, 0
        for i in range(len(nums)-1):
            temp = max(rob2, rob1+nums[i])
            rob1 = rob2 
            rob2 = temp
        val1 = rob2
        rob1, rob2 =  0, 0
        for i in range(1,len(nums)):
            temp = max(rob2, rob1+nums[i])
            rob1 = rob2 
            rob2 = temp
        val2 = rob2
        return max(val1,val2)


        



        