# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l, r = 0,1
        result = []
        
        for i in range(len(nums)):
            c = 0
            while r < len(nums):
                if nums[l] > nums[r]:
                    c +=1
                r += 1
            result.append(c)
            l+=1
            r = 0
        return result
        
               
                

            
        