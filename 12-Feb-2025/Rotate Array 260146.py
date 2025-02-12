# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        for i in range(k):
            l , r = 0,n
            item = nums.pop()
            nums.insert(0,item)
            n-=1
        return nums

            

        